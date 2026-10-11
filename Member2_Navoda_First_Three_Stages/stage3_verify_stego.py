
import subprocess
subprocess.run(["steghide", "extract", "-sf", "logo.jpeg", "-p", "stego123", "-f"], check=True)
print(open("secret.txt").read())


