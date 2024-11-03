
# MAC Address Changer

This Python script allows users to change the MAC (Media Access Control) address of a network interface on a Windows system. It is designed with a simple command-line interface, making it easy to modify MAC addresses.

## Features
- Change the MAC address of a specified network interface.
- User-friendly command-line interface for input.
  
## Prerequisites
- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Administrator privileges**: The script requires admin privileges to change network settings.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/DevBhuva/PythonForHack/tree/main/MAC_CHANGER.git
   ```

2. Navigate to the project directory:
   ```bash
   cd MAC_CHANGER
   ```

3. Make sure Python 3 is installed on your system. You can download it [here](https://www.python.org/downloads/).

## Usage
To run the script, use the following command:
```bash
python mac_changer.py -i <interface> -m <new_mac_address>
```

Replace `<interface>` with the name of your network interface (e.g., `Ethernet`) and `<new_mac_address>` with the desired MAC address (e.g., `00:11:22:33:44:55`).

### Example:
```bash
python mac_changer.py -i Ethernet -m 00:11:22:33:44:55
```

**Example Output:**
```
[+] Changing MAC address for Ethernet to 00:11:22:33:44:55
Current MAC = 00:11:22:33:44:55
[+] MAC address was successfully changed to 00:11:22:33:44:55
```

## Important Notes
- **Run as Administrator**: Make sure to run the script with administrator privileges to ensure it has permission to modify network settings.
- **Compatibility**: This script is built for Windows systems. Additional modifications may be needed to run it on Linux or macOS.
