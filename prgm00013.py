def solution(k, d):
    xs = []
    ys = []
    for i in range(0, d+1, k):
        xs.append(i)
        ys.append(i)
    xs = xs[::-1]
    answer = 0
    pop = 0
    d_sq = d**2
    for y in ys:
        xs = xs[pop:]
        print(xs)
        pop = 0
        for i, x in enumerate(xs):
            x_sq = x**2
            y_sq = y**2
            if x_sq + y_sq <= d_sq:
                answer += len(xs)-i
                if x_sq + y_sq == d_sq:
                    pop += 1
                break
            else:
                pop += 1
    return answer
    
print(solution(2,4)) # 6
print(solution(1,5)) # 26
