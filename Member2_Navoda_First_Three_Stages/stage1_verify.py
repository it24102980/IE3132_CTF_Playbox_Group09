import subprocess, re

output = subprocess.run(["git", "log", "-p"], capture_output=True, text=True, cwd="stage1_repo").stdout
flag = re.search(r"NEXUS\{[^}]+\}", output).group()
print("Flag found:", flag)
