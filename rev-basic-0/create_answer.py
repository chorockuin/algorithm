def find_input(random_val: int, target_str: str) -> int:
    # target_str 을 뒤집은 후 16진수로 변환
    rev = target_str[::-1]
    x = int(rev, 16)
    # 복호화된 입력값 반환
    return x ^ random_val

if __name__ == "__main__":
    local_30 = 0x42da14aa
    target = "a0b4c1d7"

    result = find_input(local_30, target)
    print(f"local_2c = 0x{result:08x} ({result})")
    print(f"local_2c = {result} ({result})")