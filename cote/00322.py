import math

class Solution:
    def check(self, coins, amount, memory):
        min_count = math.inf

        if amount in memory:
            return memory[amount]
        
        if amount == 0:
            return 0
        
        if amount < 0:
            return math.inf
        
        for c in coins:
            if amount >= c:
                min_count = min(min_count, self.check(coins, amount - c, memory))
        memory[amount] = min_count + 1
        return min_count + 1
                
    def coinChange(self, coins, amount):
        coins.sort(reverse=True)
        min_count = self.check(coins, amount, {})
        if min_count == math.inf:
            return -1
        return min_count
    
print(Solution().coinChange([1,2,5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1], 0))
print(Solution().coinChange([1,2,3,4,5,6,7,8,9,10,11,2**31-1], 10**4))
