from typing import List

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]

        r = []
        for i, c in enumerate(input):
            if c in '*+-':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for lv in left:
                    for rv in right:
                        r.append(eval(str(lv)+c+str(rv)))
        return r
tc1 = "2-1-1"
tc2 = "2*3-4*5"

print(Solution().diffWaysToCompute(tc2))