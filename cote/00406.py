from typing import List
import collections

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(reverse=True, key=lambda x: (x[0], -x[1]))
        r = []
        for p in people:
            o = p[1]
            r = r[:o] + [p] + r[o:]
        return r

tc1 = [[7,0], [4,4], [7,1], [5,2], [6,1], [5,0]]

print(Solution().reconstructQueue(tc1))