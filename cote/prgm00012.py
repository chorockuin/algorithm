def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def gcd_list(a):
    r = a[0]
    for n in a[1:]:
        r = gcd(r, n)
    return r

def gcd_cards(cards_a, cards_b):
    gcd_a = gcd_list(cards_a)
    if gcd_a > 1:
        for card in cards_b:
            if card%gcd_a == 0:
                return 1
        return gcd_a
    return 1

def solution(cards_a, cards_b):
    cards_a.sort()
    cards_b.sort()
    a = gcd_cards(cards_a, cards_b)
    b = gcd_cards(cards_b, cards_a)
    if a == 1 and b == 1:
        return 0
    return max(a, b)

print(solution([10, 17], [5, 20])) # 0
print(solution([10, 20], [5, 17])) # 10
print(solution([14, 35, 119], [18, 30, 102])) # 7

