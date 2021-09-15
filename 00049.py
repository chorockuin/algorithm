import collections

strings = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

c_strings = collections.defaultdict(list)
for i, s in enumerate(strings):
    c_list = []
    for c in s:
        c_list.append(c)
    c_list.sort()
    c_strings[''.join(c_list)].append(i)
print(c_strings)

ll = []
for k, v in c_strings.items():
    l = []
    for i in v:
        l.append(strings[i])
    l.sort()
    ll.append(l)
print(ll)

##

anagrams = collections.defaultdict(list)

for word in strings:
    anagrams[''.join(sorted(word))].append(word)
print(anagrams.values())

##

a = [2, 5, 1, 9, 7]
a.sort()
print(a)

b = 'zbdaf'
b = ''.join(sorted(b))
print(b)

c = ['aa', 'b', 'c', 'dddd', 'e']
c.sort(key=lambda x: len(x))
print(c)