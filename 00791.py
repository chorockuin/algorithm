class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {}
        for i, c in enumerate(order):
            order_dict[c] = i
            
        ordered_s = []        
        for c in s:
            if c in order_dict:
                ordered_s.append((c, order_dict[c]))
            else:
                ordered_s.append((c, 26))

        sorted_s = sorted(ordered_s, key=lambda x: x[1])
        return ''.join(map(str, list(map(lambda x: x[0], sorted_s))))

print(Solution().customSortString("cba", "abcd")) # cbad
print(Solution().customSortString("cbafg", "abcd")) # cbad
print(Solution().customSortString("kqep", "pekeq"))