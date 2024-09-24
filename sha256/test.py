import hashlib
import base64

# 평문
data = "hello world"
print('-- data        = ' + data)

# sha256 해시 객체 생성
hash_object = hashlib.sha256()

# ----------------------------------------------------

# 문자열을 바이트로 변환하여 해시 객체에 전달
hash_object.update(data.encode('utf-8'))

# 해시 결과를 16 진수로 출력
hash_hex = hash_object.hexdigest()
print(f"-- hash_hex    = {hash_hex}")

# ----------------------------------------------------

# 해시 결과를 base64 로 인코딩
hash_base64 = base64.b64encode(hash_object.digest()).decode('utf-8')
print(f"-- hash_base64 = {hash_base64}")
