# MACE: Multiple Application Command Executor

## Description
MACE (Multiple Application Command Executor) enables automated, parallel execution of commands across multiple targets, such as IP addresses or serial ports. This script dynamically substitutes target information into specified command templates for efficient, concurrent execution.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/williamblair333/mace.git
    ```
2. Navigate to the project directory:
    ```bash
    cd mace
    ```
3. Install any dependencies (if applicable):
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the project, use the following command:
    ```bash
    python mace.py -t <target_file> -c <command_file>
    ```

### Arguments
- `-t, --target_file`: Specifies the path to a file containing targets (IP addresses, serial ports, etc.), one per line.
- `-c, --command_file`: Indicates the file containing command templates, with `{{TARGET}}` placeholders for dynamic substitution.

### Example Commands
Execute with default settings:
    ```bash
    python mace.py -t targets.txt -c commands.txt
    python mace.py -t fw_push_targets.txt -c fw_push_commands.txt
    ```

## Files

### ip-targets.txt
    192.168.1.5
    192.168.1.6
    ...

### desktop-checks.txt
    robot --variable ip_address:{{TARGET}} --test "CPU Usage Check" util\cpu-check.robot
    robot --variable ip_address:{{TARGET}} --test "HDD Usage Check" util\hdd-check.robot
    robot --variable ip_address:{{TARGET}} --test "Check Open Ports" util\portscan.robot
    robot --variable ip_address:{{TARGET}} --variablefile util\variables-file.py util\big-big-test.robot

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes.
4. Push your branch: `git push origin feature-name`.
5. Create a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Author & Contact
William Blair  
Date: 2024-02-01  
Version: 1.3
