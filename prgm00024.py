import math

# def decimal_to_k(n, k):
#     unit = 0
#     out = 0
#     while n >= k:
#         r = n%k
#         out += r * 10**unit
#         n = int(n/k)
#         unit += 1
#     out += n * 10**unit
#     return out

# def k_string_to_decimal(k_string, k):
#     out = 0
#     for i, k_char in enumerate(k_string[::-1]):
#         out += int(k_char)*(k**i)
#     return out

def decimal_to_k_string(n, k):
    unit = 0
    out = ''
    while n >= k:
        r = n%k
        out += str(r)
        n = int(n/k)
        unit += 1
    out += str(n)
    return out[::-1]

def is_prime_decimal(x):
    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    k_string = decimal_to_k_string(n,k)
    k_strings = k_string.split('0')
    k_strings = list(filter(lambda x: len(x) > 0, k_strings))
    count = 0
    for k_string in k_strings:
        if is_prime_decimal(int(k_string)):
            count += 1
    return count

print(solution(437674, 3)) # 3
print(solution(110011, 10)) # 2
