class Solution:
    s = {}
    s[1] = 0
    s[2] = 1
    def integerReplacement(self, n: int) -> int:
        if n in self.s:
            return self.s[n]

        if n%2 == 0:
            # print(f'/2 {n/2}-')
            self.s[n] = self.integerReplacement(n/2) + 1
            return self.s[n]
        else:
            a = self.integerReplacement(n+1)
            b = self.integerReplacement(n-1)
            if (a > b):
                # print(f'-1 {n-1}-')
                self.s[n] = b + 1
            else:
                # print(f'+1 {n+1}-')
                self.s[n] = a + 1
            return self.s[n]

print(Solution().integerReplacement(1))
print(Solution().integerReplacement(8))
print(Solution().integerReplacement(7))
print(Solution().integerReplacement(4))
print(Solution().integerReplacement(2**32 -1))