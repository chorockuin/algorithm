s1 = 'babad'
s2 = 'cbbd'
s3 = '123455431'

def get_palindrom(s):
    p_l = []
    for i, c in enumerate(s):
        if len(s)%2 == 0:
            if i+1 < len(s):
                if s[i] == s[i+1]:
                    f = i
                    b = i+1
                    p = s[i:i+2]
                else:
                    continue
            else:
                continue
        else:
            f = i
            b = i
            p = ''

        while f > 0 and b+1 < len(s):
            f -= 1
            b += 1
            if s[f] == s[b]:
                p = s[f:b+1]
            else:
                break
            print(p)
        if len(p) > 0:
            p_l.append(p)
    print(p_l)

get_palindrom(s3)

##

def get_palindrom_ref(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >=0 and right <= len(s) and s[left] == s[right-1]:
            left -= 1
            right += 1
        return s[left+1:right-1]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    return result

print(get_palindrom_ref(s3))