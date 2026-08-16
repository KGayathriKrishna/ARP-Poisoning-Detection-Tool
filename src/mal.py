from scapy.all import *
import os
import random

# ===== CONFIG =====
ORIGINAL_PCAP = r"C:\Users\krish\OneDrive\Desktop\ARP\NS.pcap"
MALICIOUS_PCAPNG = r"C:\Users\krish\OneDrive\Desktop\ARP\malicious.pcapng"
TEMP_PCAP = r"C:\Users\krish\OneDrive\Desktop\ARP\temp_modified.pcap"

# ===== FUNCTIONS =====
def generate_random_mac():
    return ":".join([f"{random.randint(0, 255):02x}" for _ in range(6)])

def create_malicious_arp():
    """Create properly formatted Ethernet+ARP packets"""
    malicious_packets = PacketList()
    
    # ARP Spoofing (5 packets)
    for i in range(5):
        malicious_packets.append(
            Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(
                op=2,
                psrc="192.168.1.1",
                pdst=f"192.168.1.{i+10}",
                hwsrc=generate_random_mac()
            )
        )
    
    # ARP Flooding (100 packets)
    for _ in range(100):
        malicious_packets.append(
            Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(
                op=1,
                psrc=f"10.0.0.{random.randint(1, 254)}",
                pdst=f"10.0.0.{random.randint(1, 254)}",
                hwsrc=generate_random_mac()
            )
        )
    
    # Gratuitous ARP (3 packets)
    for _ in range(3):
        malicious_packets.append(
            Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(
                op=2,
                psrc="192.168.1.100",
                pdst="192.168.1.100",
                hwsrc=generate_random_mac()
            )
        )
    
    # Random ARP (20 packets)
    for _ in range(20):
        malicious_packets.append(
            Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(
                op=random.choice([1, 2]),
                psrc=f"192.168.1.{random.randint(1, 254)}",
                pdst=f"192.168.1.{random.randint(1, 254)}",
                hwsrc=generate_random_mac()
            )
        )
    
    print(f"[+] Created {len(malicious_packets)} malicious ARP packets")
    return malicious_packets

# ===== MAIN =====
try:
    # 1. Load original packets
    print(f"[+] Loading original capture from {ORIGINAL_PCAP}")
    original_packets = rdpcap(ORIGINAL_PCAP)
    print(f"[+] Loaded {len(original_packets)} packets")
    
    # 2. Create malicious packets
    malicious_packets = create_malicious_arp()
    
    # 3. Combine packets properly
    print("[+] Combining packets...")
    all_packets = original_packets + malicious_packets
    
    # 4. Save temporary file
    print(f"[+] Saving combined packets to {TEMP_PCAP}")
    wrpcap(TEMP_PCAP, all_packets)
    
    # 5. Convert to pcapng
    print("[+] Converting to pcapng format...")
    if os.path.exists(r"C:\Program Files\Wireshark\editcap.exe"):
        editcap = r"C:\Program Files\Wireshark\editcap.exe"
    else:
        editcap = "editcap"
    
    cmd = f'"{editcap}" -F pcapng "{TEMP_PCAP}" "{MALICIOUS_PCAPNG}"'
    if os.system(cmd) == 0:
        print(f"[✓] Success! Saved malicious pcapng to {MALICIOUS_PCAPNG}")
        os.remove(TEMP_PCAP)
    else:
        print("[!] Conversion failed. Please try manually:")
        print(f"    {cmd}")

except Exception as e:
    print(f"[!] Error ({type(e).__name__}): {e}")
    if 'TEMP_PCAP' in locals() and os.path.exists(TEMP_PCAP):
        print(f"[!] Temporary file remains at {TEMP_PCAP}")