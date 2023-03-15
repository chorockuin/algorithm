def permutation(p):
    prev_i = p[-1][0]
    prev_k = p[-1][1]

    if prev_k%2 == 0:
        k=int(prev_k/2)
    else:
        k=prev_k*3+1
    i = prev_i + 1
    
    integral = max(prev_k, k)-(abs(prev_k-k)/2.0)
    
    p.append([i,k,integral])
    
    if k <= 1:
        return
        
    permutation(p)

def solution(k, ranges):
    p = [[0,k,0.0]]
    permutation(p)
    
    answer = []
    for r in ranges:
        f = r[0]+1
        t = r[1]+len(p)
        # print(f'{p} -> from:{f}({r[0]}) to:{len(p)+t}({r[1]})')
    
        area = p[f:t]
        if f > t:
            answer.append(-1.0)
        elif f == t:
            answer.append(0.0)
        else:
            area = map(lambda x: x[2], area)
            answer.append(sum(area))
        
    return answer

print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))