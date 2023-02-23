def solution(cards):
    boxes = []
    card_indexes = {}
    for i, card in enumerate(cards):
        boxes.append([card, 0, i])
        card_indexes[i] = 0
    card = boxes[0]
    group_id = 1
    same_group_card_count = 0
    group_card_count = []
    while True:
        if card[1] == 0:
            card[1] = group_id
            card_indexes.pop(card[2])
            same_group_card_count += 1
            card = boxes[card[0]-1]
        else:
            group_card_count.append(same_group_card_count)
            if len(card_indexes) == 0:
                break
            else:
                same_group_card_count = 0
                group_id += 1
                card = boxes[list(card_indexes.keys())[0]]
    group_card_count.sort(reverse=True)
    if len(group_card_count) < 2:
        return 0
    else:
        return group_card_count[0] * group_card_count[1]

print(solution([8,6,3,7,2,5,1,4])) # 12