import hashlib
import json
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

secret_key_base64 = "nwjnt3gm4tjQXGd9w0hngSDBXXsAT9U8GcBObVA8NsY="
iv_base64 = "ZSnm22ERRX7rbT4FtYwfdQ=="


# 암호화
def aes_encrypt(plainText):
    secret_key = hashlib.sha256(secret_key_base64.encode('utf-8')).hexdigest()[0:32]
    secret_iv = hashlib.sha256(iv_base64.encode('utf-8')).hexdigest()[0:16]

    encrypter = AES.new(key=secret_key.encode('utf-8'), mode=AES.MODE_CBC, iv=secret_iv.encode('utf-8'))
    encryptedJson = encrypter.encrypt(plainText)
    output = base64.b64encode(encryptedJson).decode('utf-8')
    return output


# 복호화
def aes_decrypt(output):
    secret_key = hashlib.sha256(secret_key_base64.encode('utf-8')).hexdigest()[0:32]
    secret_iv = hashlib.sha256(iv_base64.encode('utf-8')).hexdigest()[0:16]

    decrypter = AES.new(key=secret_key.encode('utf-8'), mode=AES.MODE_CBC, iv=secret_iv.encode('utf-8'))
    decryptedJson = unpad(decrypter.decrypt(base64.b64decode(output)), block_size=32).decode('utf-8')
    return decryptedJson


plainText = {'uid': '377bfc9c17e02340282505cb6c3a4001', 'local_ip': '192.168.220.199'}
print(f"plainText => {plainText}")
plainText = pad(json.dumps({'result': True, 'file_path': plainText}).encode('utf-8'), block_size=32)
print(f"plainText => {plainText}")

encrypted = aes_encrypt(plainText)
print(f"encrypted => {encrypted}")

decrypted = aes_decrypt(encrypted)
print(f"decrypted => {decrypted}")
