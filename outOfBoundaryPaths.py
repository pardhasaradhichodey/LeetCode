class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dp (x,y,steps = maxMove):
            if x not in range(m) or y not in range(n):
                return 1
            if not steps:
                return 0
            ans, dx, dy = 0, 1, 0
            for _ in range(4):
                ans+= dp(x+dx, y+dy, steps-1)
                dx, dy = dy,-dx
            return ans
        return dp (startRow, startColumn)%1000000007