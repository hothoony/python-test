import sys
print(sys.executable)
print("sys.executable = " + sys.executable)

from aes256_util import aes_encrypt, aes_decrypt

plaintext = b"plaintext"
print(f"- plaintext: {plaintext}")

encrypted = aes_encrypt(plaintext)
print(f"- encrypted: {encrypted}")

decrypted = aes_decrypt(encrypted)
print(f"- decrypted: {decrypted}")
