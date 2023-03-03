def solution(n, k, enemy):
    killed_enemy = []
    for i in range(len(enemy)):
        killed_enemy.append(enemy[i])
        killed_enemy.sort(reverse=True)
        if len(killed_enemy) > k:
            if sum(killed_enemy[k:]) > n:
                return i
    return len(enemy)
            

print(solution(7, 3, [4,2,4,5,3,3,1])) # 5
print(solution(2, 4, [3,3,3,3])) # 4
print(solution(8, 3, [1,2,4,5,3,2,1])) # 7
print(solution(1, 1, [1,2,4,5,3,2,1])) # 2
print(solution(3, 2, [1,9,3,1,1])) # 5
print(solution(2, 4, [3,2,3,3,1,1])) # 6
print(solution(5, 1, [1,1,3,1,1,1,1])) # 6
print(solution(6, 2, [6,4,1,5,1,1,7])) # 5