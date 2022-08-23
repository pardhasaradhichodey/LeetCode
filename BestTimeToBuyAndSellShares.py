def maxProfit(prices) -> int:
        min1=10001
        max1=0
        for i in prices:
            min1=min(min1,i)
            max1=max(max1,i-min1)
        return max1
print(maxProfit(list(map(int,input().split()))))
