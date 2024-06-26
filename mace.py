"""
MACE: The Multiple Application Command Executor (In Parallel)  d

Description:
    Enables automated, parallel execution of commands across multiple targets, such as IP addresses or serial ports. 
    This script dynamically substitutes target information into specified command templates for efficient, 
    concurrent execution.

Usage:
    python mace.py -t <target_file> -c <command_file>

Arguments:
    -t, --target_file   Specifies the path to a file containing targets (IP addresses, serial ports, etc.), one per line.
    -c, --command_file  Indicates the file containing command templates, with `{{TARGET}}` placeholders for dynamic substitution.

Example Commands:
    Execute with default settings:
    python mace.py -t targets.txt -c commands.txt
    python mace.py -t fw_push_targets.txt -c fw_push_commands.txt

Requirements:
    - Python 3.x: Ensure Python 3 is installed and the script is executed within a Python 3 environment.

Author & Contact: William Blair
Date: 2024-02-01
Version: 1.3

Notes:
    - The `{{TARGET}}` placeholder within command templates allows for dynamic command execution across different targets.
"""


import argparse
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# Function to execute a command for a given target, with target-specific substitution
def run_command(target: str, command: str) -> None:
    # Substitute target placeholder with actual target value in command
    formatted_command = command.replace("{{TARGET}}", target)
    print(f"Executing Command for Target {target}: {formatted_command}")
    # Execute the command and capture output
    result = subprocess.run(formatted_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Output the result of command execution
    print(f"Command Output for Target {target}:\n{result.stdout}")

# Main function to parse arguments and execute commands in parallel
def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Run commands in parallel for multiple targets.")
    parser.add_argument('-t', '--target_file', type=str, required=True, help='Path to the file containing targets.')
    parser.add_argument('-c', '--command_file', type=str, required=True, help='File containing commands with target placeholders.')
    
    args = parser.parse_args()

    # Read targets and commands from specified files
    with open(args.target_file) as target_file:
        targets = target_file.read().splitlines()
    with open(args.command_file) as command_file:
        commands = command_file.readlines()

    # Inform the user about the start of execution
    total_targets = len(targets)
    total_commands = len(commands)
    print(f"Starting execution: {total_targets} targets and {total_commands} commands.")

    # Execute commands in parallel for each target
    with ThreadPoolExecutor() as executor:
        for i, command in enumerate(commands, start=1):
            # Log the command execution progress
            print("====================================================================================================\n")
            print(f"Now running command {i} of {total_commands} for all targets: {command.strip()}")
            futures = [executor.submit(run_command, target, command.strip()) for target in targets]
            # Ensure all futures are completed
            for future in futures:
                future.result()
            print(f"Finished running command {i} of {total_commands} for all targets.")

    # Final log indicating completion of all commands
    print("All commands executed for all targets.")

if __name__ == "__main__":
    main()