# 3 <= n <= 100,000
# 2 <= len(roads) <= 500,000
# [a,b] 1 <= a, b <= n, a != b
# 1 <= len(sources) <= 500
# 1 <= destination <= n

from collections import defaultdict

def solution(n, roads, sources, destination):
    memo = [0]*n
    
    paths = defaultdict(list)
    for r in roads:
        paths[r[0]].append(r[1])
        paths[r[1]].append(r[0])
    print(f'paths: {paths}')
        
    src_spot = defaultdict(int)
    for source in sources:
        src_spot[source] = -1
    print(f'src_spot: {src_spot}')

    dst_spot = [destination, 0]

    q = []
    q.append(dst_spot)
    memo[dst_spot[0]-1] = 1
    while len(q) > 0:
        spot = q.pop(0)
        src_spot[spot[0]] = spot[1]
        print(f'set {spot[0]} distance {spot[1]}')
        if spot[0] in paths:
            for s in paths[spot[0]]:
                if memo[s-1] == 0:
                    memo[s-1] = 1
                    print(f'search to {s} distance {spot[1]+1}')
                    q.append([s, spot[1]+1])
    answer = []
    for source in sources:
        answer.append(src_spot[source])
    return answer

print(solution(3, [[1,2], [2,3]], [2,3], 1)) # [1,2]
print(solution(5, [[1,2], [1,4], [2,4], [2,5], [4,5]], [1,3,5], 5)) # [2,-1,0]