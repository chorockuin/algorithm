# def reverse_insort(a, x):
#     i = 0
#     size = len(a)
#     while i < size:
#         mid = (i + size)//2
#         if x > a[mid]:
#             size = mid
#         else:
#             i = mid + 1
#     a.insert(i, x)

# def solution(bullet_num, bomb_num, enemy_num_list):
#     enemy_num = 0
#     top_enemy_num_list = []
#     top_enemy_num_list_sum = 0
#     for i in range(len(enemy_num_list)):
#         enemy_num += enemy_num_list[i]
#         if i < bomb_num:
#             reverse_insort(top_enemy_num_list, enemy_num_list[i])
#             top_enemy_num_list_sum += enemy_num_list[i]
#         else:
#             if enemy_num_list[i] > top_enemy_num_list[-1]:
#                 reverse_insort(top_enemy_num_list, enemy_num_list[i])
#                 top_enemy_num_list_sum += enemy_num_list[i] - top_enemy_num_list[-1]
#                 top_enemy_num_list.pop(-1)

#             if enemy_num - top_enemy_num_list_sum > bullet_num:
#                 return i
#     return len(enemy_num_list)

from queue import PriorityQueue

def solution(bullet_num, bomb_num, enemy_num_list):
    enemy_num = 0
    top_enemy_num_q = PriorityQueue()
    top_enemy_num_q_sum = 0
    for i in range(len(enemy_num_list)):
        enemy_num += enemy_num_list[i]
        if i < bomb_num:
            top_enemy_num_q.put(enemy_num_list[i])
            top_enemy_num_q_sum += enemy_num_list[i]
        else:
            min_enemy_num = top_enemy_num_q.get()
            if enemy_num_list[i] > min_enemy_num:
                top_enemy_num_q.put(enemy_num_list[i])
                top_enemy_num_q_sum += enemy_num_list[i] - min_enemy_num
            else:
                top_enemy_num_q.put(min_enemy_num)

            if enemy_num - top_enemy_num_q_sum > bullet_num:
                return i
    return len(enemy_num_list)

print(solution(7, 3, [4,2,4,5,3,3,1])) # 5
print(solution(2, 4, [3,3,3,3])) # 4
print(solution(8, 3, [1,2,4,5,3,2,1])) # 7
print(solution(1, 1, [1,2,4,5,3,2,1])) # 2
print(solution(3, 2, [1,9,3,1,1])) # 5
print(solution(2, 4, [3,2,3,3,1,1])) # 6
print(solution(5, 1, [1,1,3,1,1,1,1])) # 6
print(solution(6, 2, [6,4,1,5,1,1,7])) # 5