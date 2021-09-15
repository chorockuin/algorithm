from typing import List
import heapq
import collections

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print(nums)
        nums.pop(0)
        print(nums)
        nums.pop()
        print(nums)

        heapq.heapify(nums)
        print(nums)
        heapq.heappop(nums)
        print(nums)
        heapq.heappush(nums, 0)
        print(nums)

        x = collections.deque(nums)
        print(x)
        x.pop()
        print(x)
        x.popleft()
        print(x)



        # return sorted(nums, reverse=True)[k-1]
        #
        # h = list()
        # for n in nums:
        #     heapq.heappush(h, -n)
        # for i in range(k):
        #     r = heapq.heappop(h)
        # return -r


nums = [3,2,1,5,6,4]
k = 2
# nums = [3,2,3,1,2,4,5,5,6]
# k = 4

print(Solution().findKthLargest(nums, k))