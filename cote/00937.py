logs = ['digl 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']

num_logs = []
char_logs = []
for log in logs:
    if log.split()[1].isdigit():
        num_logs.append(log)
    else:
        char_logs.append(log)

char_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(logs)
print(char_logs + num_logs)

a = [(1, 3, 4), (0, 3, 2), (1, 5, 5), (1, 5, 2), (0, 1, 3), (2, 4, 2)]
s1 = sorted(a, key = lambda x : (x[0]))
s2 = sorted(a, key = lambda x : (x[0], x[1]))
s3 = sorted(a, key = lambda x : (x[0], -x[1]))
s3 = sorted(a, key = lambda x : (x[0], x[1], -x[2]))
print(a)
print(s1)
print(s2)
print(s3)
