# def solution(floor):
#     answer=0
#     while floor:
#         threshold=0
#         if 10 <= floor < 100:
#             threshold=6
#         else:
#             threshold=5
#         digit = floor%10
#         if digit >= threshold:
#             floor += 10-digit
#             answer += 10-digit
#         else:
#             floor -= digit
#             answer += digit
#         floor = int(floor/10)
#     return answer

import sys
sys.setrecursionlimit(10**6)

def brute_force(floor, prev_click, min_click):
    if floor == 0:
        min_click[0] = min(prev_click, min_click[0])
        return
        
    digit = floor%10
    
    olim_click = 10-digit
    berim_click = digit
    
    if floor < 10:
        brute_force(0, prev_click+olim_click+1, min_click)
    else:
        brute_force(int((floor+10-digit)/10), prev_click+olim_click, min_click)
    brute_force(int((floor-digit)/10), prev_click+berim_click, min_click)
    
def solution(floor):
    min_click = [100000000000000]
    brute_force(floor, 0, min_click)
    return min_click[0]

print(solution(1)) # 1
print(solution(16)) # 6
print(solution(15)) # 6
print(solution(254)) # 11 4+5+2->11 vs 6+4+3->13
print(solution(255)) # 12 5+5+2->12 vs 5+4+3->12
print(solution(256)) # 11 6+5+2->13 vs 4+4+3->11
print(solution(2555)) # 16 5+5+5+2->17 vs 5+4+4+3->16
print(solution(2556)) # 15 6+5+5+2->18 vs 4+4+4+3->15
print(solution(2655)) # 15 5+5+4+3->17 vs 5+4+3+3->15
print(solution(100000000)) # 1
print(solution(100000009)) # 3
