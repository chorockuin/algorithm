from typing import List

class Solution:
    max_p = -10*2*10**4
    
    def calc_max(self, memo, nums):
        if len(memo) == 0:
            return
        for i, m in enumerate(memo):
            self.max_p = max(m, self.max_p)
            memo[i] = m//nums[0]
        self.calc_max(memo[1:], nums[1:])
        
    def split_nums(self, nums):
        s_nums = []
        s = []
        for n in nums:
            if n != 0:
                s.append(n)
            else:
                s_nums.append(s)
                s = []
        s_nums.append(s)
        return s_nums
    
    def calc(self, nums):
        memo = []
        for i, n in enumerate(nums):
            if i > 0:
                memo.append(memo[i-1] * n)
            else:
                memo.append(n)
        self.calc_max(memo, nums)
                
    def maxProduct(self, nums: List[int]) -> int:
        s_nums = self.split_nums(nums)
        for ns in s_nums:
            self.calc(ns)
        if (len(s_nums) > 1):
            return max(0, self.max_p)
        return self.max_p

print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,-1]))
print(Solution().maxProduct([-2,0,3,1]))
print(Solution().maxProduct([0,-2,3,1]))
print(Solution().maxProduct([-2]))
print(Solution().maxProduct([1,0,-1,2,3,-5,-2]))
print(Solution().maxProduct([-5,2,4,1,-2,2,-6,3,-1,-1,-1,-2,-3,5,1,-3,-4,2,-4,6,-1,5,-6,1,-1,-1,1,1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,-1,1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,1,-1,1,-1,1,1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,-1,1,1,1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,-1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,1,-1,-1,1,1,1,-1,-1,1,1,-1,1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,1,-1,1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,1,-1,-1,1,-1,1,1,-1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,1,-1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,1,-1,-1,1,1,1,1,1,-1,1,-1,1,-1,-1,1,1,1,1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,1,1,1,1,-1,-1,1,1,1,-1,1,-1,1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,1,1,1,1,1,1,-1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,1,1,1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,1,1,-1,-1,-1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,1,-1,1,-1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,1,-1,1,1,1,1,1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,1,1,-1,1,1,1,1,1,-1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,1,1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,1,1,1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,-1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,1,1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,-1,1,1,1,-1,1,1,-1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,-1,1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,1,1,1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,1,1,-1,1,-1,1,-1,1,-1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,1,1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,1,1,1,1,-1,1,-1,1,1,1,1,-1,-1,-1,-1,-1,1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,-1,-1,1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,1,-1,1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,1,1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,1,-1,1,1,-1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,-1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,1,1,-1,1,1,1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,1,1,1,-1,1,1,1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,1,1,1,-1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,1,-1,-1,-1,1,1,-1,1,1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,1,1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,1,-1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1,-1,1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,-1,1,1,1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,1,1,1,1,1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,-1,1,1,1,1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,1,-1,1,1,1,1,-1,1,-1,1,-1,-1,-1,1,1,1,1,1,-1,1,1,1,1,1,1,-1,1,1,1,1,-1,1,1,-1,1,-1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,1,1,1,1,1,1,-1,1,-1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,-1,1,-1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,-1,1,-1,1,1,-1,1,-1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,1,1,1,1,-1,1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,1,1,1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,1,1,-1,-1,1,-1,1,1,-1,1,-1,1,1,-1,1,-1,1,1,1,1,-1,-1,1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,1,-1,1,-1,1,1,1,1,1,-1,1,1,1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,1,1,1,1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,1,-1,1,1,1,1,-1,-1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,1,1,1,-1,1,1,-1,1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,1,1,-1,1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,1,1,1,1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,-1,-1,1,1,1,-1,1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,1,-1,-1,-1,1,1,-1,1,1,1,1,-1,1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,-1,1,1,1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,1,-1,-1,1,1,1,-1,1,1,-1,1,1,1,1,1,-1,1,1,-1,-1,1,1,1,-1,-1,1,1,-1,1,1,-1,1,1,1,1,1,-1,-1,1,-1,-1,1,1,-1,1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,1,1,-1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,1,1,-1,1,1,1,1,-1,-1,1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,1,-1,-1,1,1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,1,-1,1,-1,-1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,-1,1,1,1,-1,1,1,-1,1,-1,1,1,1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,1,-1,-1,1,1,-1,1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,1,1,1,1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,1,1,-1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,1,1,-1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,1,1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,1,-1,1,-1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,1,-1,1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,1,1,-1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,1,-1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1,1,1,1,1,1,1,-1,-1,1,-1,1,1,-1,1,1,1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,-1,-1,1,1,1,1,1,-1,-1,-1,1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,1,-1,1,-1,1,-1,-1,1,1,1,-1,1,-1,1,1,1,-1,1,1,-1,-1,1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,1,1,1,1,1,-1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,1,1,-1,1,-1,1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,1,1,1,1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,-1,-1,1,1,1,-1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,1,1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,-1,1,1,1,-1,1,1,-1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,1,1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,1,1,1,1,-1,1,1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,-1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,1,1,-1,1,1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,-1,1,1,-1,1,1,1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,1,1,-1,-1,1,-1,1,1,-1,1,1,-1,1,1,1,1,1,-1,1,1,1,1,-1,-1,-1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,1,1,-1,1,1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,-1,1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,1,1,1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,1,1,1,1,-1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1,1,1,-1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,-1,1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,1,1,-1,1,1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,-1,-1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,1,1,-1,-1,1,1,1,1,-1,1,1,1,1,-1,1,1,1,1,-1,1,-1,-1,1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,1,1,-1,-1,1,1,1,1,1,-1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,-1,1,1,-1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,-1,1,-1,1,1,1,1,-1,-1,1,1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,1,1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,1,1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,1,1,1,-1,1,1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,-1,1,1,-1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,1,-1,1,1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,1,1,1,1,-1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,1,-1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,1,-1,1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,-1,-1,1,-1,1,1,-1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,1,-1,-1,1,1,1,1,1,-1,1,-1,-1,1,1,1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,1,1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,-1,1,1,1,-1,-1,1,1,-1,1,1,-1,1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,1,-1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,1,1,1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,1,1,-1,1,-1,1,1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,-1,-1,1,1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,1,-1,-1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,1,1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,1,1,1,1,-1,1,-1,1,-1,-1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,1,1,1,-1,1,1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,1,1,-1,1,-1,1,1,1,1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,-1,1,-1,1,1,-1,1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,-1,-1,1,1,-1,1,1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,1,-1,-1,1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,1,1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,1,1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,1,1,1,1,-1,1,1,1,1,1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,1,-1,1,1,1,-1,1,-1,-1,1,1,1,1,1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,1,1,-1,1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,1,1,1,-1,1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,1,1,1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,-1,1,1,1,1,1,-1,1,1,1,1,-1,1,-1,1,1,1,1,1,1,1,-1,-1,1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,1,1,-1,1,1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,-1,1,-1,1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,1,-1,1,1,1,1,-1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,-1,1,1,1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,1,1,-1,1,-1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,1,1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,1,-1,1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,-1,1,1,1,1,1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,1,1,-1,1,-1,1,1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,1,1,1,1,-1,1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,1,1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,-1,-1,1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,1,1,1,1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,1,-1,1,1,-1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,1,1,1,-1,1,1,1,1,-1,-1,1,-1,1,-1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,1,-1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,1,1,1,1,1,1,-1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,1,1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,1,1,-1,1,1,-1,-1,1,1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,-1,1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,1,1,1,-1,-1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,1,1,-1,1,-1,1,1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,-1,1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,1,1,-1,1,-1,1,1,-1,1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,1,-1,1,1,1,1,1,1,-1,1,-1,1,1,1,-1,1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,1,1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,1,1,-1,1,-1,-1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,1,-1,1,-1,1,-1,1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,1,1,-1,-1,1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,1,1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,1,-1,1,1,-1,1,1,1,1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,1,1,1,-1,-1,1,1,-1,1,-1,1,1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1]))
# print(Solution().maxProduct([0,10]*10**1))
