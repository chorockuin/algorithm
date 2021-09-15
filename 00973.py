from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dists = [[i, x*x + y*y] for i, (x, y) in enumerate(points)]
        dists.sort(key=lambda x:x[1])
        return [points[d[0]] for d in dists[:K]]

points = [[1,3], [-2,2]]
k = 1

# points = [[3,3],[5,-1],[-2,4]]
# k = 2


print(Solution().kClosest(points, k))