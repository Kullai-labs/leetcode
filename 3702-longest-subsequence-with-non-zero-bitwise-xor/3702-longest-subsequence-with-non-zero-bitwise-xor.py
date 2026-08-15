class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in nums:
            ans ^= i

        if ans != 0:
            return n

        for i in nums:
            if i != 0:
                return n - 1

        return 0