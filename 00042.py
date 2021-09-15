heights = [2,1,0,2,1,0,1,3,2,1,2,1]

def calc_left_volume(heights, index):
    volume = 0

    if index == 0:
        return volume

    max_h = max(heights[:index])
    if max_h == 0:
        return volume

    max_h_i = heights[:index].index(max_h)
    for i in range(max_h_i, index):
        volume += heights[max_h_i] - heights[i]

    volume += calc_left_volume(heights, max_h_i)
    return volume

def calc_right_volume(heights, index):
    volume = 0

    if index == len(heights)-1:
        return volume

    max_h = max(heights[index+1:])
    if max_h == 0:
        return volume

    max_h_i = index + 1 + heights[index+1:].index(max_h)
    for i in range(index+1, max_h_i+1):
        volume += heights[max_h_i] - heights[i]

    volume += calc_right_volume(heights, max_h_i)
    return volume

max_i = heights.index(max(heights))
print(calc_left_volume(heights, max_i) + calc_right_volume(heights, max_i))