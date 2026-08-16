# ARP Poisoning Detection & Alert Tool

## Overview

This project is a Python-based cybersecurity tool for analyzing ARP traffic and identifying possible ARP spoofing/poisoning activity.

The tool uses Scapy to process captured PCAP/PCAPNG network traffic and checks IP-MAC address mappings for suspicious changes. A Tkinter-based graphical interface displays the analysis results and provides options to open packet-capture files, save logs, clear the display, and exit the application.

## Features

- Analyze ARP packets from PCAP/PCAPNG files
- Identify ARP requests and replies
- Maintain IP-MAC address mappings
- Detect possible spoofing when an existing IP is observed with a different MAC address
- Display alerts and packet information through a GUI
- Save analysis logs to a text file
- Clear the log display

## Project Structure

```text
ARP-Poisoning-Detection-Tool/
├── README.md
├── requirements.txt
├── src/
│   ├── arp1.py
│   └── mal.py
├── pcap/
│   ├── NS.pcap
│   └── arp-poisoning.pcapng
└── docs/
    └── ARP-Spoofing-Detection-and-Alert-Tool.pptx
```

## Technology Stack

- Python
- Scapy
- Tkinter
- PCAP / PCAPNG network captures

## How It Works

1. Select a PCAP or PCAPNG file using the GUI.
2. The application reads the captured packets.
3. ARP requests and replies are identified.
4. For ARP replies, the source IP and MAC address are checked against the stored IP-MAC mapping.
5. If an IP address is observed with a different MAC address, the application reports a possible spoofing event.
6. Results are displayed in the GUI and can be saved as a text log.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/ARP-Poisoning-Detection-Tool.git
cd ARP-Poisoning-Detection-Tool
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Running the Tool

Run:

```bash
python src/arp1.py
```

Use **Open PCAP** to select a `.pcap` or `.pcapng` file for analysis.

## Project Scope

This repository is intended for academic and cybersecurity learning purposes. The supplied detector analyzes captured network traffic rather than performing unrestricted live network monitoring.

## Documentation

The `docs/` directory contains the project presentation.

## Disclaimer

Use this project only on network traffic and systems for which you have permission to perform security testing and analysis.
