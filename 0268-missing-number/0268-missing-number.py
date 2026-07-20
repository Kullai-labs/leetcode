class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=sum(nums) 
        n=len(nums)
        total=(n*(n+1))//2
        return total - s
        xor=len(nums)
        # for i in range(1,len(nums)):
        #     xor=xor^i #1,2,3
        # for val in nums:
        #     xor=xor^val
        # return xor

