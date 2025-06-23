from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        output = []
        nums_len = len(nums)
        pre_sum = sum(nums[:2*k+1])
        # print(f'{nums[:2*k+1]} pre_sum: {pre_sum}')
        for i, n in enumerate(nums):
            if i < k:
                output.append(-1)
            elif i >= nums_len-k:
                output.append(-1)
            else:
                if i > k:
                    pre_sum = pre_sum - nums[i-k-1] + nums[i+k]
                output.append(int(pre_sum/(2*k+1)))
        return output
    
print(Solution().getAverages([7,4,3,9,1,8,5,2,6], 3)) # [-1,-1,-1,5,4,4,-1,-1,-1]
print(Solution().getAverages([100000], 0)) # [100000]
print(Solution().getAverages([8], 100000)) # [-1]
print(Solution().getAverages([18334,25764,19780,92480,69842,73255,89893], 0)) # [18334,25764,19780,92480,69842,73255,89893]
print(Solution().getAverages([40527,53696,10730,66491,62141,83909,78635,18560], 2)) # [-1,-1,46717,55393,60381,61947,-1,-1]