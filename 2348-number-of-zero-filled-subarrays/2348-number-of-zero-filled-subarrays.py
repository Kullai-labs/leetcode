class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # count=0
        # n=0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         count+=1
        #     else:
        #         if count >0:
        #             n=(count*(count+1))//2
        # return n
        count=0
        total_count=0
        for i in nums:
            if i == 0:
                count+=1
                total_count+=count
            else:
                count=0
        return total_count

        