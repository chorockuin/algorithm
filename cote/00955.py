from typing import List

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        def is_sorted(string_list):
            for i in range(len(string_list)-1):
                if string_list[i] > string_list[i+1]:
                    return False
            return True

        def slice_string_list(string_list, _from, _to):
            r = []
            for string in string_list:
                r.append(string[_from:_to])
            return r

        index = 0
        while True:
            N = len(A[0])
            if N > 1:
                half_string_list = slice_string_list(A, 0, int(N/2))
            else:
                half_string_list = A

            if is_sorted(half_string_list):
                A = half_string_list
            else:
                if N > 1:
                    A = slice_string_list(A, int(N/2), N)
                    index += int(N/2)
                else:
                    index += 1
            if N == 1:
                break
        return index


tc_list = [[["xga","xfb","yfa"], 1], [["zyx","wvu","tsr"], 3], [["abcdef","uvwxyz"], 0], [["ca","bb","ac"], 1], [["xc","yb","za"], 0]]

for tc in tc_list:
    print('{} {}'.format(Solution().minDeletionSize(tc[0]), tc[1]))