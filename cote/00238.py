from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_forward = [1]
        nums_backward = [1]

        for i in range(len(nums)):
            if i > 0:
                nums_forward.append(nums_forward[i-1]*nums[i-1])
                nums_backward.append(nums_backward[i-1]*nums[len(nums)-i])
        num_backward = nums_backward[::-1]
        r = []
        for i in range(len(nums)):
            r.append(nums_forward[i]*num_backward[i])
        return r

nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))