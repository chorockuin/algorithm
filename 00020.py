class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in table:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if table[stack.pop()] != c:
                    return False
        if len(stack) > 0:
            return False
        return True

Solution().isValid('([{}])')