from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num == 0:
            return [-1, 0, 1]

        if num%3 == 0:
            mid = int(num/3)
            return [mid-1, mid, mid+1]

        return []
    
print(Solution().sumOfThree(33))
print(Solution().sumOfThree(4))