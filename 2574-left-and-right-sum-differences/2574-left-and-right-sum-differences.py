class Solution(object):
    def leftRightDifference(self, nums):
        n=len(nums)
        # leftsum=[0]*n
        # rightsum=[0]*n
        # for i in range(1,n+1):
        #     leftsum[i] = leftsum[i-1]+nums[i-1]
        # for j in range(n-2,-1,-1):
        #     rightsum[j] += rightsum[j+1]+nums[j+1]
        # for i in range(n):
        #     ans= abs(leftsum[i]-rightsum[i])
        # return ans
        result=[]
        for i in range(len(nums)):
            x=abs(sum(nums[:i])-sum(nums[i+1:]))
            result.append(x)
        return result





        