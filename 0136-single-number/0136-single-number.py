class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ans = set()
        # for num in nums:
        #     if num in ans:
        #         ans.remove(num)
        #     else:
        #         ans.add(num)
        # return ans.pop()
        xor=0
        for i in nums: 
            xor^=i
        return xor

        