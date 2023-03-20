# def solution(order):
#     order_i = 0
#     conveyor_order = [i+1 for i in range(len(order))]
#     stack = []
#     while True:
#         if len(stack) > 0 and order[order_i] == stack[-1]:
#             stack.pop()
#             order_i += 1
#         else:
#             if len(conveyor_order) == 0:
#                 return order_i
#             stack.append(conveyor_order.pop(0))
#     return order_i

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

print(solution([3, 4, 5, 1, 2])) # 3
print(solution([4, 3, 1, 2, 5])) # 2
print(solution([5, 4, 3, 2, 1])) # 5