from typing import List


class Solution:
    def my_arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum

##
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

nums = [1,4,3,2]
print(Solution().arrayPairSum(nums))