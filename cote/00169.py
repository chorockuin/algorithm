from typing import List
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # d = collections.defaultdict(int)
        # for n in nums:
        #     d[n] += 1
        #     if d[n] > int(len(nums)/2):
        #         return n
        return sorted(nums)[len(nums)//2]

tc1 = [3,2,3]
tc2 = [2,2,1,1,1,2,2]

print(Solution().majorityElement(tc1))