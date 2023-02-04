from collections import defaultdict

def solution(triangle):
    for temp_i in range(len(triangle)):
        i = (len(triangle)-1)-temp_i
        max_v = []
        for ii in range(len(triangle[i])-1):
            max_v.append(max(triangle[i][ii], triangle[i][ii+1]))
        if i > 0:
            for vi, v in enumerate(max_v):
                triangle[i-1][vi] += v
    return triangle[0][0]

print(solution([[7], [3,8], [8,1,0], [2,7,4,4], [4,5,2,6,5]]))