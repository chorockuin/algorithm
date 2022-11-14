class Solution(object):
    def countVowels(self, word):
        dp = []
        for i, el in enumerate(word):
            if el in 'aeiou':
                running_sum = i + 1 + (dp[-1] if dp else 0)
                dp.append(running_sum)
            else:
                dp.append(dp[-1] if dp else 0)
        return sum(dp)
        
print(Solution().countVowels("a"))
print(Solution().countVowels("b"))
print(Solution().countVowels("aba"))
print(Solution().countVowels("abc"))
print(Solution().countVowels("ltcd"))
print(Solution().countVowels("abab"))
print(Solution().countVowels("a" * (10 ** 5)))
