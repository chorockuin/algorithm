from typing import List

class Solution:
    max_p = -10*2*10**4
    
    def calc_max(self, memo, nums):
        if len(memo) == 0:
            return
        for i, m in enumerate(memo):
            self.max_p = max(m, self.max_p)
            if nums[0] == 0:
                memo[i] = nums[i]
            else:
                memo[i] = m // nums[0]
        self.calc_max(memo[1:], nums[1:])
    
    def maxProduct(self, nums: List[int]) -> int:
        memo = []
        for i, n in enumerate(nums):
            if i > 0:
                memo.append(memo[i-1] * n)
            else:
                memo.append(n)
        self.calc_max(memo, nums)
        return self.max_p

print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,-1]))
print(Solution().maxProduct([-2,0,3,1]))
print(Solution().maxProduct([-2]))
print(Solution().maxProduct([1,0,-1,2,3,-5,-2]))
# print(Solution().maxProduct([-10,10]*10**1))