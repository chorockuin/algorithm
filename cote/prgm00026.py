def solution(n, left, right):
    base = [i for i in range(1, n+1)]
    
    l_i = int(left/n)
    r_i = int(right/n)
    l_r = left%n
    r_r = right%n
    
    if l_i == r_i:
        answer = [l_i+1]*l_i + base[l_i:]
        answer = answer[l_r:r_r+1]
    else:
        begin = [l_i+1]*l_i + base[l_i:]
        begin = begin[l_r:]
        
        mid = []
        for i in range(l_i+1, r_i):
            mid += [i+1]*i + base[i:]
        
        end = [r_i+1]*r_i + base[r_i:]
        end = end[:r_r+1]
        answer = begin+mid+end
    return answer

print(solution(3,4,5)) # [2,3]
print(solution(3,2,5)) # [3,2,2,3]
print(solution(4,7,14)) # [4,3,3,3,4,4,4,4]
