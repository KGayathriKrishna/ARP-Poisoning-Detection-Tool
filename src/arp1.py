from scapy.all import rdpcap, ARP
from tkinter import Tk, Text, Button, Label, Scrollbar, END, VERTICAL, Frame, filedialog, messagebox
import sys

# Global variables
arp_table = {}  # For spoofing detection


# Function to handle ARP packet detection and basic spoof detection
def arp_detect(packet):
    if packet.haslayer(ARP):  # Check if the packet is an ARP packet
        output = ""  # Initialize the output message
        if packet[ARP].op == 1:  # ARP Request
            output = f"[+] ARP Request: {packet[ARP].psrc} is asking for {packet[ARP].pdst}"
        elif packet[ARP].op == 2:  # ARP Reply
            src_ip = packet[ARP].psrc  # Source IP address
            src_mac = packet[ARP].hwsrc  # Source MAC address
            # Check for spoofing
            if src_ip in arp_table:  # If the IP is already in the ARP table
                if arp_table[src_ip] != src_mac:  # If the MAC address has changed
                    output = f"[!] Possible Spoofing Detected: {src_ip} has changed MAC from {arp_table[src_ip]} to {src_mac}"
            else:  # If the IP is not in the ARP table
                arp_table[src_ip] = src_mac  # Add the IP-MAC mapping to the ARP table

            output = output or f"[+] ARP Reply: {src_mac} has address {src_ip}"

        if output:  # If there is an output message
            log_text.insert(END, output + "\n")  # Display the message in the GUI
            log_text.see(END)  # Scroll to the end of the log


# Process packets from a .pcap file
def process_pcap(file_path):
    try:
        packets = rdpcap(file_path)  # Read packets from the .pcap file
        for packet in packets:
            arp_detect(packet)  # Process each packet
        log_text.insert(END, f"[+] Finished processing {file_path}\n")
    except Exception as e:
        log_text.insert(END, f"[!] Error processing file: {e}\n")


# Open and process a .pcap file
def open_pcap():
    file_path = filedialog.askopenfilename(filetypes=[("PCAP files", "*.pcap *.pcapng")])
    if file_path:
        log_text.insert(END, f"[+] Processing file: {file_path}\n")
        process_pcap(file_path)


# Exit the app
def exit_app():
    root.destroy()
    sys.exit(0)


# Save log to a file
def save_log():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(log_text.get(1.0, END))
            messagebox.showinfo("Success", f"Log saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# Clear log display
def clear_log():
    log_text.delete(1.0, END)


# ---------- GUI Setup ----------
root = Tk()
root.title("ARP Detection Tool")
root.geometry("700x500")
root.configure(bg="#1e1e2f")

# Title Label
title_label = Label(root, text="ARP Detection & Spoofing Alert Tool", bg="#1e1e2f",
                    fg="#ffffff", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Create frame for log display
frame = Frame(root, bg="#1e1e2f")
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Text widget for logging
log_text = Text(frame, wrap="word", font=("Consolas", 11), bg="#282c34", fg="#ffffff", insertbackground="#ffffff")
log_text.pack(side="left", fill="both", expand=True)

# Scrollbar
scrollbar = Scrollbar(frame, orient=VERTICAL, command=log_text.yview)
scrollbar.pack(side="right", fill="y")
log_text.config(yscrollcommand=scrollbar.set)

# Buttons frame
button_frame = Frame(root, bg="#1e1e2f")
button_frame.pack(fill="x", pady=10)

# Buttons with styling
btn_style = {"font": ("Helvetica", 12), "bg": "#4CAF50", "fg": "white", "activebackground": "#45a049",
             "activeforeground": "white", "relief": "raised", "bd": 2, "width": 15, "padx": 5, "pady": 5}

open_button = Button(button_frame, text="Open PCAP", command=open_pcap, **btn_style)
open_button.pack(side="left", padx=10)

save_button = Button(button_frame, text="Save Log", command=save_log, **btn_style)
save_button.pack(side="left", padx=10)

clear_button = Button(button_frame, text="Clear Log", command=clear_log, **btn_style)
clear_button.pack(side="left", padx=10)

exit_button = Button(button_frame, text="Exit", command=exit_app, **btn_style)
exit_button.pack(side="right", padx=10)

# Run the GUI loop
root.mainloop()