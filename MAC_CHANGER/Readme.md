# MAC Address Changer

This Python script allows users to change the MAC (Media Access Control) address of their network interface on a Windows system.

## Features
- Change the MAC address of a specified network interface.
- Simple command-line interface for easy use.
  
## Prerequisites
- Python 3.x
- Administrator privileges on the system.
  
## Installation
1. Clone this repository:
   ```bash
   git clone https://https://github.com/DevBhuva/PythonForHack/tree/main/MAC_CHANGER.git
## Navigate to the project directory:
2. Navigate to the project directory:

   ```bash
   cd MAC_CHANGER
3. Make sure you have Python 3 installed. You can download it from here.

## Usage
- To run the script, use the following command:
    ```bash
    python mac_changer.py

- The script will prompt you to enter:
    - The network interface name.
    - The new MAC address you want to assign.

## Example:
  ```bash
      interface >Ethernet
      new MAC>00:11:22:33:44:55
- The script will then attempt to change the MAC address for the specified interface.
```

## Example Output:
   ```bash
[+] Changing MAC address for Ethernet to 00:11:22:33:44:55
```


## Important Notes
- Run as Administrator: Ensure that you run the script with administrator privileges, or it will not have the required permissions to change the MAC address.
- Compatibility: This script currently works on Windows systems. To use it on Linux or MacOS, modifications will be needed.
