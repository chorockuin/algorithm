class Solution:
    def move(self, r, c, d):
        if d > self.max_d:
            return 0
        if r < 0 or c <0 or r >= self.m or c >= self.n:
            return 1
        self.q.append([r,c,d])
        return 0
    
    def findPaths(self, m: int, n: int, max_d: int, r: int, c: int) -> int:
        self.m = m
        self.n = n
        self.q = []
        self.v = [[0]*n]*m
        self.max_d = max_d
        
        self.q.append([r,c,0])
        output = 0
        while len(self.q) > 0:
            r,c,d = self.q.pop(0)
            output += self.move(r,c-1,d+1)
            output += self.move(r-1,c,d+1)
            output += self.move(r,c+1,d+1)
            output += self.move(r+1,c,d+1)
        return output
    
print(Solution().findPaths(2,2,2,0,0))
print(Solution().findPaths(1,3,3,0,1))
print(Solution().findPaths(7,5,10,5,0))
