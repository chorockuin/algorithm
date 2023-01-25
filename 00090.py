from typing import List
from collections import defaultdict

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        output = [[]]
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]: # 현재 번호가 반복되지 않은, 유니크한 번호라면
                output_len = len(output) # 현재까지 만들어 놓은 output의 길이를 저장해 둠
            # output을 하나씩 indexing 하면서 새로운 번호 nums[i]를 추가해 줄것임
            # indexing이 중요한데, output의 index 0부터가 아닌, 유니크한 번호로 시작되는 output의 index부터다
            # 새로운 번호 nums[i]가 유니크하지 않은 번호였다면, 기존에 유니크했던 번호로 시작되는 output의 index 뒤에 그냥 붙여주기만 하면 된다
            for j in range(len(output)-output_len, len(output)):
                output.append(output[j] + [nums[i]]) # output에 nums[j]를 추가한다
        return output

print(Solution().subsetsWithDup([1,2,2]))
print(Solution().subsetsWithDup([1,2,2,3]))
print(Solution().subsetsWithDup([0]))