import sys
print(sys.executable)
print("sys.executable = " + sys.executable)

from aes256_util2 import aes_encrypt, aes_decrypt

plaintext = "Hello, World! python"
print(f"- plaintext  = {plaintext}")

encrypted = aes_encrypt(plaintext)
print(f"- encrypted  = {encrypted}")

decrypted = aes_decrypt(encrypted)
print(f"- decrypted  = {decrypted}")

print(f"- decrypted2 = {aes_decrypt('SVgal/KSz2A5+gYHxnJBe+vrmNg65fFnkViWgWBVvIs=')}")
print(f"- decrypted2 = {aes_decrypt('Cv4iyNbYEAe3my2AFiNPklgdmS27WMo9x9Wb3OSP/+0=')}")
