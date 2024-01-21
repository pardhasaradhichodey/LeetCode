class Solution:
    def countOfPairs(self, n: int, x: int, y: int):
        if x > y: x, y = y, x
        ans = [0] * (n + 2)
        x -= 1
        y -= 1
        for i in range(n):
            l, r = i + 1, n - 1
            while l <= r:
                m = (l + r) // 2
                if m - i < abs(i - x) + abs(m - y) + 1:
                    l = m + 1
                else:
                    r = m - 1
            ans[1] += 1
            ans[r+1-i] -= 1
            
            if l == n: continue
            end = y
            val = abs(i - x) + 1
            # val + 1, val + 2, ..., val + y - l
            ans[val + 1] += 1
            ans[val + y - l + 1] -= 1
            
            # val, val + 1, ..., val + n - 1 - y
            ans[val] += 1
            ans[val + n - y] -= 1
        ans = list(accumulate(ans))
        return [x * 2 for x in ans[1:-1]]