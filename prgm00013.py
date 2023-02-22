# def solution(k, d):
#     xs = []
#     ys = []
#     for i in range(0, d+1, k):
#         xs.append(i)
#         ys.append(i)
#     xs = xs[::-1]
#     answer = 0
#     pop = 0
#     d_sq = d**2
#     for y in ys:
#         xs = xs[pop:]
#         print(xs)
#         pop = 0
#         for i, x in enumerate(xs):
#             x_sq = x**2
#             y_sq = y**2
#             if x_sq + y_sq <= d_sq:
#                 answer += len(xs)-i
#                 if x_sq + y_sq == d_sq:
#                     pop += 1
#                 break
#             else:
#                 pop += 1
#     return answer

# def solution(k, d):
#     xs = []
#     ys = []
#     for i in range(0, d+1, k):
#         xs.append(i)
#         ys.append(i)
#     xs = xs[::-1]
#     center_i = 0
#     for i, x in enumerate(xs):
#         if x**2 + x**2 <= d**2:
#             center_i = i
#             break
#     center = len(xs)-center_i
#     side = 0
#     for yi, y in enumerate(ys):
#         for xi, x in enumerate(xs):
#             if y > x:
#                 break            
#             if x**2 + y**2 <= d**2:
#                 side += len(xs)-xi-yi
#                 break
#     answer = (side-center) * 2 + center
#     return answer

# def solution(k, d):
#     xs = []
#     ys = []
#     for i in range(0, d+1, k):
#         xs.append(i)
#         ys.append(i)
#     xs = xs[::-1]
#     xs_len = len(xs)
#     center_xi = 0
#     for i, x in enumerate(xs):
#         if x**2 + x**2 <= d**2:
#             center_xi = i
#             break
#     center = (xs_len-center_xi)*(xs_len-center_xi)
#     side = 0
#     for yi in range(0, xs_len-center_xi):
#         for xi in range(0, center_xi):
#             if xs[xi]**2 + ys[yi]**2 <= d**2:
#                 side += 1
#     answer = side * 2 + center
#     return answer

def solution(k, d):
    xs = []
    ys = []
    for i in range(0, d+1, k):
        xs.append(i)
        ys.append(i)
    xs = xs[::-1]
    xs_len = len(xs)
    center_xi = 0
    for i, x in enumerate(xs):
        if x**2 + x**2 <= d**2:
            center_xi = i
            break
    center = (xs_len-center_xi)*(xs_len-center_xi)
    side = 0
    for yi in range(0, xs_len-center_xi):
        for xi in range(0, center_xi):
            if xs[xi]**2 + ys[yi]**2 <= d**2:
                side += 1
    answer = side * 2 + center
    return answer

print(solution(2,4)) # 6
print(solution(1,5)) # 26
