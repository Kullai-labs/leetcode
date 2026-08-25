class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # mis=0
        # for i in range(1,len(nums)+1):
        #     n=k*i
        #     mis=0
        #     if n not in nums:
        #         mis=n
        #         break
        # return mis
        i=1
        while k>0:
            n=k*i
            if n not in nums:
                return n
            i+=1

        