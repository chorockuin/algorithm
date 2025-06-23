def solution(max_truck_num_on_bridge, max_weight, truck_weights):
    sec = 0
    q = []
    q_time = []
    while len(truck_weights) > 0:
        q_time = list(map(lambda x: x+1, q_time))
        if q_time:
            if q_time[0] >= max_truck_num_on_bridge:
                q.pop(0)
                q_time.pop(0)
            
        q.append(truck_weights[0])
        q_time.append(0)
        if sum(q) <= max_weight and len(q) <= max_truck_num_on_bridge:
            truck_weights.pop(0)
        else:
            q.pop()
            q_time.pop()            
        sec += 1
    answer = sec + max_truck_num_on_bridge
    return answer

print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))