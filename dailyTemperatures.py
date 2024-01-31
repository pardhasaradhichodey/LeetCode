class Solution:
    def dailyTemperatures(self, temperatures):
        l=len(temperatures)
        res=[0]*l
        a=[[temperatures[0],0]]
        for i in range(1,l):
            if a[-1][0]<temperatures[i]:
                while(a and a[-1][0]<temperatures[i]):
                    temp=a[-1][1]
                    res[temp]=i-temp
                    a.pop()
                a.append([temperatures[i],i])
            else:
                a.append([temperatures[i],i])
        return res