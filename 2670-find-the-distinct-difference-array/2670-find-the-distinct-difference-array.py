class Solution(object):
    def distinctDifferenceArray(self, nums):

        result = []
        for i in range(len(nums)):
            left = len(set(nums[:i+1]))
            right  = len(set(nums[i+1:]))
            result.append(left - right)
        return result

        