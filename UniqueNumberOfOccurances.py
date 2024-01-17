class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        d1={}
        for i in arr:
            d1[i]=d1.get(i,0)+1
        temp=list(d1.values())
        l1=len(temp)
        l2=len(set(temp))
        return l1==l2