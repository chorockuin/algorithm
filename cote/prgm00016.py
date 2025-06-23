from collections import defaultdict

def solution(topping):
    my_tp = defaultdict(int)
    my_i = 0
    
    ur_tp = defaultdict(int)
    ur_i = len(topping)-1
    
    tp_num = len(topping)
    
    while tp_num > 0:
        my_tp_num = len(my_tp)
        ur_tp_num = len(ur_tp)
        
        if my_tp_num <= ur_tp_num:
            my_tp[topping[my_i]] += 1
            my_i += 1
            tp_num -= 1
        elif my_tp_num > ur_tp_num:
            ur_tp[topping[ur_i]] += 1
            ur_i -= 1
            tp_num -= 1
            
    n = 0
    while len(my_tp) >= len(ur_tp):
        if len(my_tp) == len(ur_tp):
            n += 1
        my_tp[topping[ur_i]] -= 1
        if my_tp[topping[ur_i]] == 0:
            my_tp.pop(topping[ur_i])
        ur_tp[topping[ur_i]] += 1
        ur_i -= 1
    return n

print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
print(solution([1, 2, 1, 3, 5, 4, 1, 2])) # 0
print(solution([1, 2, 3, 1, 4])) # 0
print(solution([1, 1, 1, 1, 1, 2, 1, 1, 1, 2])) # 3
print(solution([1])) # 0
print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) # 9
print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 2])) # 1
print(solution([1, 2, 3, 3, 3, 4])) # 1
