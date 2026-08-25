class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)+2):
            n=k*i
            if n not in nums:
                return n
                # break
        # return mis
        # i=1
        # while k>0:
        #     n=k*i
        #     if n not in nums:
        #         return n
        #     i+=1

        