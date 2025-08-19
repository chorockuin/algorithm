from pwn import *

# 로컬 바이너리 실행
p = process(["./a.out"])

for _ in range(50):
    line = p.recvline(timeout=1).decode().strip()  # "123+456=?"
    # 예외/타임아웃 대비
    if not line or '+' not in line:
        print("unexpected line:", line)
        break

    left, rest = line.split('+', 1)
    right = rest.split('=', 1)[0]
    ans = int(left) + int(right)

    p.sendline(str(ans))

# 결과(플래그) 받기
print(p.recvall(timeout=2).decode(errors='ignore'))
