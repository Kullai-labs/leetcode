class Solution(object):
    def findGCD(self, nums):
        s=min(nums)
        l=max(nums)
        while s!=0:
            l,s=s,l%s
        return l
        