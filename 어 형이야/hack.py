def get_dot_count_list():
    with open("어 형이야/main.bro", "r", encoding="utf-8") as f:
        return f.read()
        dot_count_list = []
        dot_count = 0
        for c in f.read():
            if c == '.':
                dot_count += 1
            else:
                if dot_count > 0:
                    dot_count_list.append(dot_count)
                dot_count = 0
        return dot_count_list
    
import re

RAW = get_dot_count_list()

def b45decode_digits(digs):
    out = bytearray()
    i = 0
    while i < len(digs):
        if i + 2 < len(digs):
            x = digs[i] + 45*digs[i+1] + (45**2)*digs[i+2]
            out.append((x // 256) & 0xFF)
            out.append(x & 0xFF)
            i += 3
        elif i + 1 < len(digs):
            x = digs[i] + 45*digs[i+1]
            out.append(x & 0xFF)
            i += 2
        else:
            break
    return bytes(out)

def extract_blocks(text):
    # '혀(어*)엉' 뒤에 점(.)들이 있을 수도 있으니 함께 캡처
    pat = re.compile(r"(혀(어*)엉)(\.+)?")
    return list(pat.finditer(text))

def try_rule(name, digs):
    # 모든 값이 0..44인지 '엄격' 검증 (아니면 폐기)
    if not digs or any(d<0 or d>44 for d in digs):
        return None, f"[{name}] 불가: 0..44 범위 밖 값 존재/데이터 부족"
    data = b45decode_digits(digs)
    s = data.find(b"DH{")
    if s != -1:
        e = data.find(b"}", s+3)
        if e != -1:
            return data[s:e+1].decode('ascii','replace'), f"[{name}] OK"
    return None, f"[{name}] Base45 OK, 그러나 'DH{{...}}' 없음"

blocks = extract_blocks(RAW)
ks = [len(m.group(2) or "") for m in blocks]          # 규칙 A: '어' 개수
Ls = [len(m.group(1)) for m in blocks]                # 규칙 B: 블록 길이
dots = [len(m.group(3) or "") for m in blocks]        # 규칙 C: 뒤 '.' 개수

candidates = {
    "A-0base(어개수)": ks,
    "A-1base(어개수-1)": [k-1 for k in ks],
    "B-0base(길이)": Ls,
    "B-1base(길이-1)": [x-1 for x in Ls],
    "C-0base(점개수)": dots,
    "C-1base(점개수-1)": [d-1 for d in dots],
}

any_hit = False
for tag, seq in candidates.items():
    flag, info = try_rule(tag, seq)
    if flag:
        print(flag)
        any_hit = True
        break
    else:
        print(info)

if not any_hit:
    print("\n※ 위 규칙(억지 없음)으로는 'DH{...}'가 나오지 않습니다.")
