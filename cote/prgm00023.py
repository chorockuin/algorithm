def solution(q1, q2):
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    
    max_len = len(q1)+len(q2)
    
    if (q1_sum + q2_sum)%2 == 1:
        return -1
    
    q1_i = 0
    q2_i = 0
    
    times = 0
    while True:
        if q1_sum == q2_sum:
            break
        
        if q1_sum > q2_sum:
            q1_sum -= q1[q1_i]
            q2_sum += q1[q1_i]
            q2.append(q1[q1_i])
            q1_i += 1
            if q1_i >= len(q1) or q1_i >= max_len:
                return -1
        else:
            q2_sum -= q2[q2_i]
            q1_sum += q2[q2_i]
            q1.append(q2[q2_i])
            q2_i += 1
            if q2_i >= len(q2) or q1_i >= max_len:
                return -1
        times += 1
    return times

print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7
print(solution([1, 1], [1, 5])) # -1
print(solution([4, 2], [3, 7])) # -1