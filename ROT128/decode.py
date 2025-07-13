def decrypt_byte(b):
    return b - 128 if b >= 128 else b + 128

# 텍스트로 저장된 hex 문자열 읽기
with open("ROT128/encfile", "r") as f:
    hex_str = f.read().strip()  # "09D0CEC78D8A..." 형태

# 2자리씩 끊어서 정수 리스트로 변환
encrypted_bytes = [int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)]

# 복호화
decrypted = bytes([decrypt_byte(b) for b in encrypted_bytes])

# 복호화된 PNG 파일 저장
with open("ROT128/decode.png", "wb") as f:
    f.write(decrypted)