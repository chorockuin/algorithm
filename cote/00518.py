class Solution:
    def check(self, amount, coins, memory, stack):
        count = 0

        if amount == 0:
            # print(f'{stack}')
            if stack: stack.pop()
            return 1

        if amount < 0:
            if stack: stack.pop()
            return 0

        for i, coin in enumerate(coins):
            if amount >= coin:
                stack.append(coin)
                if amount - coin in memory and coin in memory[amount-coin]:
                    c = memory[amount-coin][coin]
                else:
                    c = self.check(amount - coin, coins[i:], memory, stack)
                    if amount-coin in memory:
                        memory[amount-coin][coin] = c
                    else:
                        memory[amount-coin] = {coin: c}
                count += c
        if stack: stack.pop()
        return count

    def change(self, amount, coins):
        if amount == 0:
            return 1

        coins.sort(reverse=True)

        return self.check(amount, coins, {}, [])

print(Solution().change(5, [1,2,5])) # 4
print(Solution().change(3, [2])) # 0
print(Solution().change(0, [1])) # 1
print(Solution().change(9, [2,3,5])) # 3
print(Solution().change(10, [10])) # 1
print(Solution().change(500, [1,2,5])) # 12701
print(Solution().change(500, [3,5,7,8,9,10,11]))
# print(Solution().change(5000, [i+1 for i in range(300)]))