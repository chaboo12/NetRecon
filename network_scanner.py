from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
from tabulate import tabulate

target_ip = "192.168.1.0/24"

arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether / arp

print("Scanning network...\n")

result = srp(packet, timeout=3, verbose=0)[0]

devices = []

for sent, received in result:
    mac = received.hwsrc

    try:
        vendor = MacLookup().lookup(mac)
    except:
        vendor = "Unknown"

    devices.append([received.psrc, mac, vendor])

print(tabulate(devices, headers=["IP Address", "MAC Address", "Vendor"]))

