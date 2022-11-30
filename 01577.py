from typing import List

class Solution:
    def memorize(self, nums):
        m = {}
        for i, i_val in enumerate(nums):
            for j_val in nums[i+1:]:
                if i_val*j_val in m:
                    m[i_val*j_val] += 1
                else:
                    m[i_val*j_val] = 1
        return m
                
    def calc(self, nums1, nums2):
        m2 = self.memorize(nums2)
        count = 0
        for i in nums1:
            if i**2 in m2:
                count += m2[i**2]
        return count
        
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.calc(nums1, nums2) + self.calc(nums2, nums1)
                    
print(Solution().numTriplets([7,4], [5,2,8,9]))
print(Solution().numTriplets([1,1], [1,1,1]))
print(Solution().numTriplets([7,7,8,3], [1,2,9,7]))
print(Solution().numTriplets([1]*1000, [1]*1000))