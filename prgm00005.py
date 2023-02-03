import math

def calculate(minute, fees):
    base_time = fees[0]
    base_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    
    if minute <= base_time:
        return base_fee
    else:
        return base_fee + (math.ceil((minute-base_time)/unit_time) * unit_fee)

def solution(fees, records):
    d = {}
    for r in records:
        time, num, _ = r.split()
        
        hm = time.split(':')
        h = int(hm[0])
        m = int(hm[1])
        time = h * 60 + m
                
        if num in d:
            d[num].append(time)
        else:
            d[num] = [time]
    for k, v in d.items():
        if len(v)%2 == 1:
            d[k].append(23*60+59)
                        
    d = sorted(d.items())
    
    answer = []
    for v in d:
        minute = 0
        for i in range(0, len(v[1]), 2):
            minute += v[1][i+1]-v[1][i]
        answer.append(calculate(minute, fees))
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
