#문자열 뒤집기

def reverse_str_by_logic(s: list) -> None:
    idx = 0
    while(idx < len(s)/2):
        t = s[idx]
        s[idx] = s[len(s)-1-idx]
        s[len(s)-1-idx] = t
        idx += 1
    print(s)

reverse_str_by_logic(['h', 'e', 'l', 'l', 'o'])
reverse_str_by_logic(['H', 'a', 'n', 'n', 'a', 'h'])

def reverse_str(s: list) -> None:
    s.reverse()
    print(s)

reverse_str(['h', 'e', 'l', 'l', 'o'])
reverse_str(['H', 'a', 'n', 'n', 'a', 'h'])