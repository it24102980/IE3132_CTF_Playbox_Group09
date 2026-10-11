import base64

def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + 13) % 26 + base)
        else:
            result += char
    return result

# 1. Read the scrambled file
with open("intercepted_memo.txt", "r") as f:
    text = f.read().strip()

# 2. Reverse Operation 2: Apply ROT13 again (it reverses itself)
b64_text = rot13(text)

# 3. Reverse Operation 1: Base64 Decode
plaintext = base64.b64decode(b64_text).decode()

# 4. Print the result
print(plaintext)