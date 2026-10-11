Operation: Shadow Ledger – CTF Project

Project Overview

Our group developed a six-stage Capture The Flag (CTF) challenge called Operation: Shadow Ledger. The idea was to create a scenario where players investigate a suspicious developer and follow different clues to uncover what happened.

Players need to complete each stage in order. The challenges cover Git history analysis, web security, steganography, cryptography, network forensics, and SSH security. Each stage provides information needed to move on to the next one.

Team Members and Responsibilities

Our group members worked on different parts of the project, including the infrastructure, individual challenges, and documentation.

Vitharana I.N.S.** – Team Leader, Infrastructure and Integration
Navoda M.M.** – Stages 1–3: OSINT, Web Security, and Steganography
Rasanjana S.P.** – Stages 4–6: Cryptography, Forensics, and System Access
S.W. Wikramathilake** – Documentation, Video Production, and Design Fidelity

System Setup and Network Configuration

We used VirtualBox to set up the lab environment. All the virtual machines were connected through a Host-Only network so that the testing could take place in an isolated environment.

We used three virtual machines for the project:

| Virtual Machine | IP Address | Main Purpose |

| Kali Linux | `192.168.56.10` | Used for scanning, testing, and forensic analysis |
| Ubuntu 24.04 Desktop | `192.168.56.21` | Runs the CTFd Docker container and the Apache web server |
| Metasploitable 2 | `192.168.56.23` | Used for the final SSH security challenge |

The CTFd portal runs on port 80, while the Stage 2 Apache web server uses port 8080.

Changes Made During Implementation

In Assignment 01, we planned to run the CTFd container on an Ubuntu Server virtual machine. During implementation, we decided to use Ubuntu 24.04 Desktop instead.

The Desktop environment was more convenient for deploying challenge files, troubleshooting issues, and recording the demonstration video. We kept the same Host-Only network setup and security controls, so the change did not affect our intended network isolation.

Deployment and Setup

Before starting the challenges, we configured the virtual machines and checked their network connections.

We used Docker Compose to start the CTFd portal and `systemctl` to manage the Apache web server. We also checked that the required services were running before testing the challenges.

For example, the Apache service can be started with:

bash
sudo systemctl start apache2

If the service stops unexpectedly, it can be restarted using:

bash
sudo systemctl restart apache2


Challenge Walkthrough

The project contains six stages. Each stage focuses on a different security concept.

Stage 1 – The Rogue Developer's Footprint

Topic: OSINT and Git history analysis

Players inspect a Git repository and look for information left behind by a developer. The challenge involves examining the repository history to find the required clue.

Stage 2 – The Unsecured Dashboard

Topic: Web security

Players investigate a login portal and examine its HTML source code to identify exposed information.

Stage 3 – The Hidden Message

Topic: Steganography

Players use Steghide and a recovered password to extract a hidden message from an image.

Stage 4 – The Intercepted Memo

Topic: Cryptography

Players reverse a custom ROT13 and Base64 encoding process to recover the target IP address.

Stage 5 – The Network Leak

Topic: Network forensics

Players examine a PCAP file in Wireshark to find an unencrypted HTTP POST request containing leaked credentials.

Stage 6 – The Source Vault

Topic: System access and SSH security

Players use the credentials recovered from the previous stage to access the target server over SSH and locate the master flag.

Tools and Technologies

The main tools used in this project were:

- VirtualBox – To run the virtual machines.
- Docker and Docker Compose – To deploy CTFd.
- CTFd – To manage the challenges, flags, and stage dependencies.
- Apache2 – To host the Stage 2 web challenge.
- Kali Linux – For security testing and investigation.
- Wireshark – To inspect network traffic.
- Steghide – To extract hidden information from images.
- Python and Paramiko – For solver scripts and SSH-related tasks.
- Git – To manage the challenge repository and inspect its history.

Repository Contents

The repository contains the challenge files and supporting materials used for the project.

Challenge Artifacts – Files provided to players, including PCAP files, images, and ZIP archives.
Python Solver Scripts – Scripts created to solve and test the challenges.
CTFd Export – A JSON export of the CTFd configuration and challenge dependencies.

These files help document how the challenges were built and provide the materials needed to reproduce and test the environment.
