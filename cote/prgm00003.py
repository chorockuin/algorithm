import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict

def get_min_count(x, y, n, memo):
    if y in memo:
        return memo[y]
    if y < x:
        return -1
    if x == y:
        return 0        
    c = []
    if y%3 == 0:
        d3 = get_min_count(x, y/3, n, memo)
        if d3 >= 0:
            c.append(d3)
    if y%2 == 0:
        d2 = get_min_count(x, y/2, n, memo)
        if d2 >= 0:
            c.append(d2)
    mn = get_min_count(x,y-n, n, memo)
    if mn >= 0:
        c.append(mn)
    if len(c) > 0:
        memo[y] = min(c)+1
        return min(c)+1
    memo[y] = -1
    return -1

def solution(x, y, n):
    memo = defaultdict(int)
    return get_min_count(x,y,n,memo)

print(solution(10,40,5)) # 2
print(solution(10,40,30)) # 1
print(solution(2,5,4)) # -1
