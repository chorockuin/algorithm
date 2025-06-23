def find_char(char, skip, index):
    char_idx = ord(char)-ord('a')
    c = 0
    i = 0
    while c < index:
        i += 1
        if (char_idx+i)%26 not in skip:
            c += 1
    return chr((char_idx+i)%26+ord('a'))

def solution(s, skip, index):
    skip = list(map(lambda x: ord(x)-ord('a'), skip))
    answer = []
    for c in s:
        answer.append(find_char(c, skip, index))
    return ''.join(a for a in answer)

print(solution("aukks", "wbqd", 5))