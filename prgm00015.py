def can_go(pos, n, m):
    y = pos[0]
    x = pos[1]
    if y >= 0 and y < n and x >= 0 and x < m:
        return True
    return False

def bfs(maps):
    n = len(maps)
    m = len(maps[0])

    q = [[0, 0, 1]]
    maps[0][0] = 0

    while len(q) > 0:
        inf = q.pop(0)

        y = inf[0]
        x = inf[1]
        c = inf[2]

        if y == n-1 and x == m-1:
            return c
        
        for pos in [[y, x-1], [y, x+1], [y-1, x], [y+1, x]]:
            if can_go(pos, n, m) and maps[pos[0]][pos[1]] == 1:
                q.append([pos[0], pos[1], c+1])
                maps[pos[0]][pos[1]] = 0
    return -1

def solution(maps):
    return bfs(maps)

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))