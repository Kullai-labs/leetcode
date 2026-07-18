class Solution(object):
    def findGCD(self, nums):
        s=min(nums)
        l=max(nums)
        while l:
            s,l=l,s%l
        return s
        