import subprocess
import optparse
import re

def get_arguments():
    parses = optparse.OptionParser()
 
    parses.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parses.add_option("-m", "--mac", dest="New_MAC", help="New MAC Address")
    
    (options, arguments)= parses.parse_args()
    if not options.interface:
        parses.error("[-] Please specify an interface, use --help for more info")
    elif not options.New_MAC:
        parses.error("[-] Please specify a new MAC address, use --help for more info")
    return options    
    
    
def change_mac(inteface, new_mac):
    print("[+] Changing MAC address for" + interface + " to "+ new_mac)
    
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
        
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


options = get_arguments()
currect_mac=get_current_mac(options.interface)
print("Current MAC = " + str(currect_mac))
change_mac(options.interface, options.New_MAC)

currect_mac = get_current_mac(options.interface)
if currect_mac == options.New_MAC:
    print("[+] MAC address was successfully changed to " + currect_mac)
else:
    print("[-] MAC address did not get changed.")   

