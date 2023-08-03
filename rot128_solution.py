# 16진수 리스트
hex_list = [(hex(i)[2:].zfill(2).upper()) for i in range(256)]

# encfile 열기
with open('encfile', 'r') as f:
    enc_s = f.read()

# 두 자리씩 쪼개서 리스트 생성
enc_list = []
for i in range(0, len(enc_s), 2):
    enc_list.append(enc_s[i:i+2])

# 평문과 관련된 리스트
plain_list = list(range(len(enc_list)))

# 원래 값으로 되돌리기
for i in range(len(enc_list)):
    hex_b = enc_list[i]
    index = hex_list.index(hex_b)
    plain_list[i] = hex_list[(index + 128) % len(hex_list)]

# 바이트로 변환
for i in range(len(plain_list)):
    plain_list[i] = int(plain_list[i], 16)
plain_s = bytes(plain_list)

# flag.png 생성
with open('flag.png', 'wb') as f:
    f.write(plain_s)