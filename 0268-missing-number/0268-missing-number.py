class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # s=sum(nums) 
        # n=len(nums)
        # total=(n*(n+1))//2
        # return total - s
        # for i in nums:
        xor=len(nums)
        for i in range(1,len(nums)):
            xor=xor^i
        for val in nums:
            xor=xor^val
        return xor

