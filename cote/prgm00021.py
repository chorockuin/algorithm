def solution(order):
    stack = []
    convy_i = 0
    i = 0
    while i < len(order):
        if len(stack) > 0:
            if stack[-1] == order[i]:
                stack.pop(-1)
                i += 1
            elif stack[-1] > order[i]:
                return i
            else:
                convy_i += 1
                stack.append(convy_i)
        else:
            convy_i += 1
            stack.append(convy_i)
    return i