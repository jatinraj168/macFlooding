# MAC Flooding Script

This project demonstrates a **MAC Flooding attack** to overwhelm a network switch's Content Addressable Memory (CAM) table by sending a large number of packets with random MAC and IP addresses. The script is intended for educational purposes and should be used responsibly.

---

## 🚨 Disclaimer

This script is for **educational and testing purposes only**. Unauthorized use of this script to disrupt or harm networks is unethical and may violate laws or organizational policies. Use it only in a controlled environment or with explicit permission.

---

## 🔧 Requirements

- Python 3.x
- **Scapy** library for packet manipulation
- Root privileges (for raw packet sending)
- A valid network interface

---

## 📁 Files

- `macFlooding.py`: The main script for generating and sending random packets.
- `README.md`: Documentation (you’re reading it!).

---

## 🛠 Installation

1. **Install Scapy**:
   ```bash
   pip install scapy
   ```
Clone the Repository (or copy the script):

```bash
Copy code
git clone https://github.com/your-repo/macflooding.git
cd macflooding
```
Set Permissions: Ensure the script has execution permission:

```bash
Copy code
chmod +x macFlooding.py
```
## 🚀 Usage
1. Identify Network Interfaces
Run the following command to list available network interfaces:

```bash
Copy code
ip link show
```
Choose a valid interface (e.g., eth0, wlan0, tap0, etc.).

## 2. Run the Script
Execute the script with root privileges to send packets:

```bash
Copy code
sudo python3 macFlooding.py
```
3. Customization
Number of Packets: Adjust the num_packets variable in the script:
```bash
Copy code
num_packets = 5000
```
Interface: Update the interface variable in the script:
```python
Copy code
interface = 'eth0'
```
## ⚙️ How It Works
Generate Packets: The script generates random Ethernet frames with random MAC and IP addresses using Scapy's RandMAC and RandIP.

Send Packets: Using sendp, it sends the packets at high speed on the specified network interface.

Objective: Overwhelming the switch's CAM table forces it into a "flooding" state, making it behave like a hub and sending packets to all connected devices.

💡 Example Output
```csharp
Copy code
Generating 10000 packets...
Sending packets on interface eth0...
Packet sending completed.
```
🛡 Safety Tips
Use in a Test Environment: Do not run this on a production network.
Avoid Unintended Targets: Ensure you're testing only on systems you own or have permission to test.
Legal Compliance: Check the laws and regulations in your area before conducting network tests.
