class Solution:
    def findContentChildren(self, g, s) -> int:
        l=len(s)
        g.sort(reverse=True)
        s.sort(reverse=True)
        res=0
        temp=0
        for i in s:
            while temp<len(g):
                if i>=g[temp]:
                    res+=1
                    temp+=1
                    break
                else:
                    temp+=1
        return res
                
