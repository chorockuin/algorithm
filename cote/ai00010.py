def solution(goods, boxes):
    goods.sort()
    boxes.sort()
    
    max_goods_count = 0
    box_index = 0
    
    for goods_size in goods:
        while box_index < len(boxes) and goods_size > boxes[box_index]:
            box_index += 1
        if box_index == len(boxes):
            break
        max_goods_count += 1
        box_index += 1
        
    return max_goods_count

print(solution([5,3,7], [3,7,6])) # 3
print(solution([1,2], [2,3,1])) # 2
print(solution([3,8,6], [5,6,4])) # 2
print(solution([3], [5])) # 1
print(solution([1,2,3,4,5,6,7], [5])) # 1
print(solution([3,4,5,6,7], [2])) # 0
print(solution([10, 30, 20], [30, 10, 20])) # 3
print(solution([9, 7, 16, 4, 8], [8, 3, 14, 10, 10])) # 4
