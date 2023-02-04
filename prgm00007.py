import heapq

def solution(scoville, K):
    heap_scv = []
    for s in scoville:
        heapq.heappush(heap_scv, s)
    
    answer = 0
    while heap_scv[0] < K:
        if len(heap_scv) == 1:
            return -1        
        low_0 = heapq.heappop(heap_scv)
        low_1 = heapq.heappop(heap_scv)
        heapq.heappush(heap_scv, low_0 + low_1 * 2)
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7)) # 2
