class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max1=0
        dict1={}
        b=False
        for i in s:
            if dict1.get(i,0)==0:
                for j in dict1.keys():
                    dict1[j]+=1
                dict1[i]=1
            else:
                b=True
                max1=max(dict1[i]-1,max1)
                for j in dict1.keys():
                    dict1[j]+=1
        if b:
            return max1
        else:
            return -1
