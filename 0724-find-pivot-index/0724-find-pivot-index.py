class Solution(object):
    def pivotIndex(self, nums):
        sum=0
        left=0
        for i in range(len(nums)):
            sum+=nums[i]
        for i in range(len(nums)):
            if left == (sum-nums[i]-left):
                return i

            left+=nums[i]
        return -1
        


        
        