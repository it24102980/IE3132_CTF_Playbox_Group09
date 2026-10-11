import re


def main():
    pcap_file = "nexus_traffic.pcap"
    print(f"[*] Reading forensic evidence: {pcap_file}...")

    try:
        # Open the PCAP in binary mode ('rb')
        with open(pcap_file, "rb") as f:
            data = f.read()

        # 1. Extract Username (Updated to match 'username=')
        user_match = re.search(rb'username=([^&]+)', data)
        username = user_match.group(1).decode() if user_match else "Not found"

        # 2. Extract Password (Updated to match 'password=')
        pass_match = re.search(rb'password=([^&]+)', data)
        password = pass_match.group(1).decode() if pass_match else "Not found"

        # 3. Extract Flag
        flag_match = re.search(rb'(NEXUS\{[^}]+\})', data)
        flag = flag_match.group(1).decode() if flag_match else "Not found"

        print("\n[+] Leaked credentials found in HTTP POST payload!")
        print(f"[+] Username: {username}")
        print(f"[+] Password: {password}")
        print(f"[SUCCESS] Stage 5 Flag: {flag}\n")

    except FileNotFoundError:
        print(f"[!] Error: {pcap_file} not found. Please generate it first.")


if __name__ == "__main__":
    main()