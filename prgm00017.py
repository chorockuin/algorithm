def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: -x[0])
    data.sort(key=lambda x: x[col-1])
    
    s_data = []
    for i, r in enumerate(data):
        s = 0
        for c in r:
            s += c % (i+1)
        s_data.append(s)
        
    answer = 0
    for s in s_data[row_begin-1:row_end]:
        answer = answer^s
    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3)) # 4