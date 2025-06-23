import sys
sys.setrecursionlimit(10**5)

def dfs(y, x, map):
    if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]):
        return 0
    if map[y][x][1] == 1:
        return 0
    
    # print(y, x, map[y][x][0])
    map[y][x][1] = 1

    l = dfs(y, x-1, map)
    t = dfs(y-1, x, map)
    r = dfs(y, x+1, map)
    b = dfs(y+1, x, map)
    return map[y][x][0] + l + t + r + b

def solution(str_map):
    # print(str_map)

    map = []
    for str_row in str_map:
        row = []
        for i in range(len(str_row)):
            if str_row[i] == 'X':
                row.append([-1, 1])
            else:
                row.append([int(str_row[i]), 0])
        map.append(row)
    # print(map)

    answer = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            # print(y, x)
            v = dfs(y, x, map)
            if v > 0:
                answer.append(v)
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))
print(solution(["123","456","789", "1XX"]))
