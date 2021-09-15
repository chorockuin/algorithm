from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_p = max(prices)
        for p in prices:
            if p < min_p:
                min_p = p
            max_profit = max(max_profit, p - min_p)
        return max_profit

prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))