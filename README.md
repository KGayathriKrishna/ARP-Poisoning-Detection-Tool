# ARP Poisoning Detection & Alert Tool

## Overview

The **ARP Poisoning Detection & Alert Tool** is an academic cybersecurity project developed to analyze captured ARP network traffic and identify possible ARP spoofing/poisoning activity.

The project has two main components:

1. **ARP Detection & Alert Tool (`arp1.py`)**  
   A Tkinter-based GUI application that reads PCAP/PCAPNG files, analyzes ARP requests and replies, maintains IP-MAC address mappings, and flags possible spoofing when an existing IP address is observed with a different MAC address.

2. **Malicious ARP Traffic Generator (`mal.py`)**  
   A Scapy-based script that creates synthetic ARP traffic for testing the detection tool, including ARP spoofing, ARP flooding, gratuitous ARP, and randomized ARP packets.

> **Note:** The detection application analyzes previously captured PCAP/PCAPNG files. It does not perform live packet capture in its current implementation.

## Features

- Analyze ARP packets from PCAP/PCAPNG files
- Identify ARP requests and ARP replies
- Maintain IP-MAC address mappings
- Detect possible spoofing when an IP address is associated with a different MAC address
- Display detection results through a graphical interface
- Save analysis logs to a text file
- Clear the log display
- Generate synthetic ARP traffic for controlled testing
- Combine normal captured traffic with generated ARP test traffic

## Project Structure

```text
ARP-Poisoning-Detection-Tool/
├── README.md
├── requirements.txt
├── src/
│   ├── arp1.py
│   └── mal.py
└── pcap/
    ├── NS.pcap
    └── arp-poisoning.pcapng
```

## Technology Stack

- **Language:** Python
- **Packet Analysis:** Scapy
- **GUI:** Tkinter
- **Network Capture Format:** PCAP / PCAPNG
- **Optional Tool:** Wireshark `editcap` for PCAP-to-PCAPNG conversion in `mal.py`

## How the Detection Tool Works

The detection application follows this basic process:

1. Open the application.
2. Select a `.pcap` or `.pcapng` file using **Open PCAP**.
3. The application reads the captured packets using Scapy.
4. ARP requests and replies are identified.
5. For ARP replies, the source IP and MAC address are checked against the stored IP-MAC mapping.
6. If an IP address that already exists in the mapping is observed with a different MAC address, the application reports a **possible spoofing event**.
7. Results are displayed in the GUI log.
8. The log can be saved as a `.txt` file.

## Testing Component

The `mal.py` script is used to generate synthetic ARP traffic for controlled testing.

It generates:

- ARP spoofing packets
- ARP flooding packets
- Gratuitous ARP packets
- Randomized ARP packets

The generated packets can be combined with an existing packet capture to create a test capture for the detection application.

## Installation

Clone the repository:

```bash
git clone https://github.com/KGayathriKrishna/ARP-Poisoning-Detection-Tool.git
cd ARP-Poisoning-Detection-Tool
```

Install the Python dependency:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the external Python dependency required by the project:

```text
scapy
```

Tkinter and the other modules used by the scripts are part of the Python standard library on typical Python installations.

## Running the Detection Tool

Run:

```bash
python src/arp1.py
```

The GUI provides options to:

- **Open PCAP** to select a `.pcap` or `.pcapng` capture
- **Save Log** to save the analysis output
- **Clear Log** to clear the displayed results
- **Exit** to close the application

## Running the Test Traffic Generator

Before running `mal.py`, update the PCAP file paths in the script to match the location of your local files.

The script currently uses Windows-specific file paths for the original capture, temporary capture, and generated PCAPNG file.

Run:

```bash
python src/mal.py
```

`mal.py` uses Scapy to generate and combine packets. It can use Wireshark's `editcap` utility to convert the resulting PCAP file to PCAPNG format. If `editcap` is not available, the conversion step will fail and the command can be run manually after installing Wireshark.

## Sample Packet Captures

The `pcap/` directory contains packet captures used with the project:

- `NS.pcap` - captured network traffic used as input/test data
- `arp-poisoning.pcapng` - ARP-related test capture used for analysis

Only analyze packet captures that you are authorized to use.

## Project Scope

This project is intended for academic cybersecurity and network-security learning. It demonstrates packet analysis, ARP protocol behavior, IP-MAC mapping, basic spoofing detection, synthetic attack-traffic generation, and GUI-based security monitoring.

## Disclaimer

Use this project only in controlled environments and on network traffic or systems for which you have permission to perform security testing and analysis.
