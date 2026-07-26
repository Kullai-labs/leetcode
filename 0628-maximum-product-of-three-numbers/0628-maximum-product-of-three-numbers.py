class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # max_p=float('-inf')
       
        # for i in range(len(nums)):
        #     prod=1
        #     for j in range(i,len(nums)):
        #         prod=nums[j]*prod
        #         if j-i+1==3:
        #             max_p=max(max_p,prod)
        # return max_p
        nums.sort()
        a=nums[-1]*nums[-2]*nums[-3]
        b=nums[0]*nums[1]*nums[-1]
        return max(a,b)
        