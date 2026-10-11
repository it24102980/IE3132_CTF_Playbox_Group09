Operation: Shadow Ledger - CTF Infrastructure
Project Overview
Operation: Shadow Ledger is a 6-stage, chain-reaction Capture The Flag (CTF) environment designed to simulate a corporate incident response scenario. Players must trace a rogue developer's digital footprint, bypass hidden portals, decrypt intercepted communications, and ultimately secure the Nexus Tech network.
Team Members & Roles
Vitharana I.N.S. (Team Leader / Infrastructure & Integration)
Navoda .M.M (Stages 1-3: OSINT, Web Security, Steganography)
Rasanjana S.P. (Stages 4-6: Cryptography, Forensics, System Access)
S.W. Wikramathilake (Documentation, Video Production & Design Fidelity)
Architecture & Infrastructure
The environment is built on an isolated VirtualBox Host-Only Network (192.168.56.0/24) to ensure safe, contained exploitation.
Virtual Machine Topology:
Kali Linux (Attacker): 192.168.56.10 - Used for network scanning, exploitation, and forensic analysis.
Ubuntu 24.04 Desktop (Portal & Web Host): 192.168.56.21 - Hosts the CTFd Docker container (Port 80) and the Stage 2 Apache Web Server (Port 8080).
Metasploitable 2 (Target Server): 192.168.56.23 - Hosts the final SSH vulnerability and the master flag vault.
Note on Design Fidelity (Assignment 1 vs. Assignment 2):
During implementation, we deployed the CTFd Docker container on the Ubuntu 24.04 Desktop VM instead of the originally planned Ubuntu Server VM. This deviation was made to provide a more user-friendly workspace for rapid artifact deployment, debugging, and video capture, while maintaining the exact same Host-Only network isolation and Docker functionality outlined in our initial design.
Deployment & Setup Guide
Network Configuration
Ensure all VMs are connected to the VirtualBox "Host-Only Adapter".
Ubuntu-24: sudo netplan apply
Kali Linux: sudo nmcli con up "Wired connection 2" (or equivalent host-only interface).
Metasploitable 2: sudo ifconfig eth0 192.168.56.23 netmask 255.255.255.0
2. Starting the Services
On Ubuntu-24 (CTFd & Apache):
Start the CTFd Portal
cd ~/CTFd
sudo docker compose up -d
Start the Apache Web Server (Stage 2)
sudo systemctl start apache2
#Access the portal at: http://192.168.56.21
#On Metasploitable 2 (SSH Target):
#Ensure the SSH service is running and the dev_admin user is active.
#sudo service ssh start
Stage Walkthrough (Solution Overview)
The challenges are strictly locked via CTFd dependencies. Players must solve them in order:
#Stage 1: The Rogue Developer's Footprint (OSINT)
Concept: Git history analysis.
Action: Extract a deleted .env file from a provided repository zip using git log -p.
#Stage 2: The Unsecured Dashboard (Web Security)
Concept: Client-side information leakage.
Action: Inspect the HTML source code of a login portal to find hardcoded developer credentials.
#Stage 3: The Hidden Message (Steganography)
Concept: Data hiding in image files.
Action: Use steghide with a recovered password to extract a hidden Base64 payload from a company logo.
#Stage 4: The Intercepted Memo (Cryptography)
Concept: Custom obfuscation algorithms.
Action: Reverse a custom ROT13 and Base64 encoding pipeline to reveal a target IP address.
#Stage 5: The Network Leak (Forensics)
Concept: Network traffic analysis.
Action: Analyze a PCAP file in Wireshark to find an unencrypted HTTP POST request containing leaked credentials.
#Stage 6: The Source Vault (System Access)
Concept: SSH Exploitation / Privilege Escalation.
Action: Use the credentials from Stage 5 to SSH into the target server and read the master flag from a hidden directory.
Tools & Technologies Used
Infrastructure: VirtualBox, Docker, Docker Compose, Apache2, Netplan.
Platform: CTFd (v3.x).
Offensive/Forensic Tools: Kali Linux, Wireshark, Scapy (Python), Steghide, Paramiko (Python SSH), Git.
Repository Contents:
Challenge_Artifacts/: Files provided to players (PCAPs, Images, Zips).
Python_Solver_Scripts/: Automated scripts developed by the team to solve each stage (LO3 Compliance).
CTFd_Export/: JSON backup of the CTFd configuration and dependencies.
