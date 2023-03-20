def solution(q1, q2):
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    
    if (q1_sum + q2_sum)%2 == 1:
        return -1
    
    times = 0
    while True:
        if q1_sum == q2_sum:
            break
        elif q1_sum > q2_sum:
            q1_sum -= q1[0]
            q2_sum += q1[0]
            q2.append(q1[0])
            q1 = q1[1:]
            if len(q1) == 0:
                return -1
        else:
            q2_sum -= q2[0]
            q1_sum += q2[0]
            q1.append(q2[0])
            q2 = q2[1:]
            if len(q2) == 0:
                return -1
        times += 1
    return times

print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7
print(solution([1, 1], [1, 5])) # -1