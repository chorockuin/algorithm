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

    while len(q) > 0:
        inf = q.pop(0)

        y = inf[0]
        x = inf[1]
        c = inf[2]

        if y == n-1 and x == m-1:
            return c
        
        maps[y][x] = 0
        
        for pos in [[y, x-1], [y, x+1], [y-1, x], [y+1, x]]:
            if can_go(pos, n, m) and maps[pos[0]][pos[1]] == 1:
                q.append([pos[0], pos[1], c+1])
    return -1

def dfs_sub(pos, n, m, maps):
    y = pos[0]
    x = pos[1]
    
    if can_go(pos, n, m) == False or maps[y][x] == 0:
        return False
    
    if y == n-1 and x == m-1:
        return True
    
    maps[y][x] = 0
    
    return dfs_sub([y, x-1], n, m, maps) or dfs_sub([y, x+1], n, m, maps) or dfs_sub([y-1, x], n, m, maps) or dfs_sub([y+1, x], n, m, maps)
    

def dfs(maps):
    n = len(maps)
    m = len(maps[0])
    
    return dfs_sub([0, 0], n, m, maps)
    
import copy

def solution(maps):
    m1 = copy.deepcopy(maps)
    m2 = copy.deepcopy(maps)
    if dfs(m1):
        return bfs(m2)
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))