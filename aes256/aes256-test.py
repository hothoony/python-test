import sys
print(sys.executable)
print("sys.executable = " + sys.executable)

from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Base64로 인코딩된 secretKey와 iv
secret_key_base64 = "Base64_Encoded_SecretKey"
iv_base64 = "Base64_Encoded_IV"

# Base64 디코딩
secret_key = b64decode(secret_key_base64)
iv = b64decode(iv_base64)

# AES-256 암호화
cipher = AES.new(secret_key, AES.MODE_CBC, iv)
plaintext = b"plaintext"
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
ciphertext_base64 = b64encode(ciphertext).decode()
print(f"Encrypted (Base64): {ciphertext_base64}")

# AES-256 복호화
cipher = AES.new(secret_key, AES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(b64decode(ciphertext_base64)), AES.block_size)
print(f"Decrypted: {decrypted.decode()}")
