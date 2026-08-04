class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s=sum(nums)
        min1=min(nums)
        max1=max(nums)
        res=[]
        # mx=max(nums)
        for i in range(min1,max1):
            if i  not in nums:
                res.append(i)
        return res
       
        