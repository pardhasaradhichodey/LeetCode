class Solution:
    def minimumPushes(self, word: str) -> int:
        s=[0]*26
        for i in word:
            s[ord(i)-97]+=1
        s.sort(reverse=True)
        print(s)
        res=0
        for i in range(8):
            res+=s[i]
            if s[i]==0:
                return res
        print(res)
        for i in range(8,16):
            res+=(s[i]*2)
            if s[i]==0:
                return res
        print(res)
        for i in range(16,24):
            res+=(s[i]*3)
            if s[i]==0:
                return res
        for i in range(24,26):
            res+=(s[i]*4)
            if s[i]==0:
                return res
        return res
        