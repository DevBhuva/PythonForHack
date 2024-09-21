import subprocess

interface = input("interface >")
new_mac= input("new MAC>")
print("[+] Changing MAC address for" + interface + " to "+ new_mac)

subprocess.call("ipconfig"+ interface +" down", shell=True)
subprocess.call("ipconfig"+ interface +" hw ether "+ new_mac, shell=True)
subprocess.call("ipconfig"+ interface +" up ", shell=True)