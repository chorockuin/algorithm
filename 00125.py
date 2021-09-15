#유효한 펠린드롬

def is_palindrome_by_using_list(s: str) -> bool:
    t = []
    for c in s:
        if c.isalnum():
            t.append(c.lower())

    while(len(t) > 1):
        if t.pop(0) != t.pop():
            return False
    return True

print(is_palindrome_by_using_list('A man, a plan, a canal: Panama'))
print(is_palindrome_by_using_list('race a car'))

import collections
def is_palindrome_by_using_deque(s: str) -> bool:
    t = collections.deque()
    for c in s:
        if c.isalnum():
            t.append(c.lower())

    while(len(t) > 1):
        if t.popleft() != t.pop():
            return False
    return True

print(is_palindrome_by_using_deque('A man, a plan, a canal: Panama'))
print(is_palindrome_by_using_deque('race a car'))

import re
def is_palindrome_by_using_re(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]

print(is_palindrome_by_using_re('A man, a plan, a canal: Panama'))
print(is_palindrome_by_using_re('race a car'))