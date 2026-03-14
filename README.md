NetRecon 🔍


NetRecon is a Python-based network reconnaissance tool that scans a local network to discover active devices. It identifies connected devices and displays useful information such as IP address, MAC address, and device manufacturer.

---

🚀 Features

- Discover devices connected to the local network
- Display IP address of each device
- Retrieve MAC address of devices
- Identify manufacturer using MAC vendor lookup
  

---

🛠 Technologies Used

- Python
- Scapy
- MAC Vendor Lookup
- Tabulate

---

⚙️ Installation

Install the required Python libraries:

pip install scapy
pip install mac-vendor-lookup
pip install tabulate

---

▶️ How to use

Run the program:

python network_scanner.py

The scanner will analyze the network and list all active devices.

---

📊 Example Output

IP Address      MAC Address         Vendor

192.168.1.1     BC:62:D2:CB:2D:E8   Router
192.168.1.5     8C:8B:5B:41:84:E9   Laptop
192.168.1.10    7A:55:B1:4D:98:21   Samsung

---

🎯 Learning Objectives

This project demonstrates important networking and cybersecurity concepts:

- Network reconnaissance
- ARP scanning
- Device discovery
- MAC address vendor identification
