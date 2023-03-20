def cantor(n, bits):
    if n == 0:
        return bits
    
    bits_len = len(bits)
    for i in range(bits_len):
        if bits[i] == '1':
            bits += '11011'
        else:
            bits += '00000'
    bits = bits[bits_len:]
    n -= 1
    return cantor(n, bits)

def solution(n, l, r):
    answer = 0
    bits = "1"
    bits = cantor(n, bits)
    bits = bits[l-1:r]
    for bit in bits:
        answer += int(bit)
    return answer

print(solution(2, 4, 17)) # 8
