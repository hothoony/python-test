import hashlib
import base64
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import json

# Base64로 인코딩된 secretKey와 iv
secret_key_base64 = "nwjnt3gm4tjQXGd9w0hngSDBXXsAT9U8GcBObVA8NsY="
iv_base64 = "ZSnm22ERRX7rbT4FtYwfdQ=="

# AES-256 암호화
def aes_encrypt(plaintext):
    # SHA-256 해시를 사용하여 key와 iv 생성
    key = hashlib.sha256(secret_key_base64.encode('utf-8')).hexdigest()[:32]  # 32바이트
    iv = hashlib.sha256(iv_base64.encode('utf-8')).hexdigest()[:16]    # 16바이트

    # AES 암호화
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    encrypted_data = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))

    # Base64로 인코딩하여 반환
    encrypted_base64 = base64.b64encode(encrypted_data).decode('utf-8')
    return encrypted_base64

# AES-256 복호화
def aes_decrypt(encrypted_data):
    # SHA-256 해시를 사용하여 key와 iv 생성
    key = hashlib.sha256(secret_key_base64.encode('utf-8')).hexdigest()[:32]  # 32바이트
    iv = hashlib.sha256(iv_base64.encode('utf-8')).hexdigest()[:16]    # 16바이트

    # Base64로 디코딩 후 AES 복호화
    encrypted_data_bytes = base64.b64decode(encrypted_data)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    decrypted_data = unpad(cipher.decrypt(encrypted_data_bytes), AES.block_size)

    # UTF-8로 변환하여 반환
    decrypted_str = decrypted_data.decode('utf-8')
    
    try:
        # JSON 형식일 경우 파싱
        return json.loads(decrypted_str)
    except json.JSONDecodeError:
        return decrypted_str
