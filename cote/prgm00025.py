def explore_dungeons(hp, dungeons, history, depth):
    max_depth = depth
    for i, d in enumerate(dungeons):
        if i in history:
            continue
        if hp < d[0]:
            continue
        hp -= d[1]
        history.append(i)
        max_depth = max(max_depth, explore_dungeons(hp, dungeons, history, depth+1))
        history.pop()
        hp += d[1]
    return max_depth

def solution(hp, dungeons):
    history = []
    return explore_dungeons(hp, dungeons, history, 0)

print(solution(80, [[80,20],[50,40],[30,10]])) # 3
