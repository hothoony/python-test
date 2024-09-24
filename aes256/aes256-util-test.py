import sys
print(sys.executable)
print("sys.executable = " + sys.executable)

from aes256_util import aes_encrypt, aes_decrypt

plaintext = "Hello, World!"
print(f"- plaintext  = {plaintext}")

encrypted = aes_encrypt(plaintext)
print(f"- encrypted  = {encrypted}")

decrypted = aes_decrypt(encrypted)
print(f"- decrypted  = {decrypted}")

print(f"- decrypted2 = {aes_decrypt('mFiqTEFaBE61Bydoz5sN9Q==')}")
