from pwn import *

HOST = "host8.dreamhack.games"
PORT = 15167

p = remote(HOST, PORT)

for _ in range(50):
    line = p.recvline(timeout=1).decode().strip()
    if not line or '+' not in line:
        print("unexpected line:", line)
        break

    left, rest = line.split('+', 1)
    right = rest.split('=', 1)[0]
    ans = int(left) + int(right)

    p.sendline(str(ans))

print(p.recvall(timeout=2).decode(errors='ignore'))
