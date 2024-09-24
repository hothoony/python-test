from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Base64로 인코딩된 secretKey와 iv
secret_key_base64 = "nwjnt3gm4tjQXGd9w0hngSDBXXsAT9U8GcBObVA8NsY="
iv_base64 = "ZSnm22ERRX7rbT4FtYwfdQ=="

# AES-256 암호화
def aes_encrypt(plaintext):
    
    key = b64decode(secret_key_base64)
    iv = b64decode(iv_base64)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    
    encrypted_base64 = b64encode(encrypted_data).decode('utf-8')
    return encrypted_base64

# AES-256 복호화
def aes_decrypt(encrypted_data):
    
    key = b64decode(secret_key_base64)
    iv = b64decode(iv_base64)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(b64decode(encrypted_data)), AES.block_size)
    
    return decrypted.decode('utf-8')
