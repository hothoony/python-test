from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# from Cryptodome.Cipher import AES
# from Cryptodome.Random import get_random_bytes

import base64

secret_key = 'your-secret-key'.ljust(32)  # 32 bytes for AES-256
iv = get_random_bytes(16)

def encrypt(plain_data):
    cipher = AES.new(secret_key.encode(), AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plain_data.ljust(32).encode())  # Padding to 32 bytes
    return base64.b64encode(iv + ciphertext).decode('utf-8')

def decrypt(enc_data):
    enc_data = base64.b64decode(enc_data)
    iv = enc_data[:16]
    ciphertext = enc_data[16:]
    cipher = AES.new(secret_key.encode(), AES.MODE_CBC, iv)
    return cipher.decrypt(ciphertext).decode('utf-8').strip()

encrypted_text = encrypt("Hello World")
decrypted_text = decrypt(encrypted_text)
