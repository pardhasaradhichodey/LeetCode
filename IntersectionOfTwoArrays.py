def IntersectionOfTwoArrays(nums1,nums2):
    d1={}
    d2={}
    for i in range(len(nums1)):
        if nums1[i] not in d1:
            d1[nums1[i]]=1
        else:
            d1[nums1[i]]+=1
    for i in range(len(nums2)):
        if nums2[i] not in d2:
            d2[nums2[i]]=1
        else:
            d2[nums2[i]]+=1
    ans=[]
    for key in d1:
        if key in d2:
            ind=min(d1[key],d2[key])
            while ind>0:
                ans.append(key)
                ind-=1
    return ans
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
print(IntersectionOfTwoArrays(nums1,nums2))
