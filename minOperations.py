class Solution:
    def minOperations(self, s: str) -> int:
        s1="01"
        s2="10"
        r1=0
        r2=0
        l=len(s)
        if l%2==0:
            t1=s1*(l//2)
            t2=s2*(l//2)
        else:
            t1=s1*(l//2)+"0"
            t2=s2*(l//2)+"1"
        for i in range(l):
            if s[i]!=t1[i]:
                r1+=1
            if s[i]!=t2[i]:
                r2+=1
        return min(r1,r2)