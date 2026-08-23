class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max1=float('-inf')
        # for i  in range(len(nums)):
        #     s=0
        #     for j in range(i,len(nums)):
        #         # s=sum(nums[i:j+1])
        #         s+=nums[j]
        #         max1=max(max1,s)
        # return max1
        current=nums[0]
        best=nums[0]
        for i in nums[1:]:
            current=max(i,current+i)
            best=max(best,current)
        return best