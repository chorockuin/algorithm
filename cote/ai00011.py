from collections import Counter

def solution(card):
    lost_cards = []
    card_counter = Counter(card)
    for card_num, card_count in card_counter.items():
        if card_count%2 == 1:
            lost_cards.append(card_num)
    lost_cards.sort()
    return lost_cards


print(solution([1,3,2,5,3,1])) # [2,5]
print(solution([1,3,5,2,3,1])) # [2,5]
print(solution([1,2,3,4,4,3,2,5])) # [1,5]