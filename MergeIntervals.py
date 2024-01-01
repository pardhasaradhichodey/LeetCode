class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort()
        temp=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]>temp[1]: 
                res.append(temp)
                temp=intervals[i]
            else:
                if temp[1]<intervals[i][1]:
                    temp[1]=intervals[i][1]
        res.append(temp)
        return res
