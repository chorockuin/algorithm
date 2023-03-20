def solution(elements):
    sum = []
    for idx in range(len(elements)):
        x = 0
        for inc in range(len(elements)):
            i = (idx+inc)%len(elements)
            x += elements[i]
            sum.append(x)
            # print(x)
    sum = set(sum)
    answer = len(sum)
    return answer

print(solution([7,9,1,1,4]))
