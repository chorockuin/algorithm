from collections import Counter

def solution(n, tangerine):
    tg_cnt = Counter(tangerine)
    tg_cnt = sorted(tg_cnt.items(), key = lambda item: -item[1])
    cnt = 0
    for i, x in enumerate(tg_cnt):
        cnt += x[1]
        if cnt >= n:
            return i+1
            
print(solution(6, [1,3,2,5,4,5,2,3])) # 3
print(solution(4, [1,3,2,5,4,5,2,3])) # 2
print(solution(2, [1,1,1,1,2,2,2,3])) # 1