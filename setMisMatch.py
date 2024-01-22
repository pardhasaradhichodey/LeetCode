class Solution:
    def findErrorNums(self, nums):
        s=sum(list(set(nums)))
        s1=sum(nums)
        l=len(nums)
        l=l*(l+1)//2
        return [s1-s,l-s]