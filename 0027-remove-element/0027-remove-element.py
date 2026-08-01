class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # for i in nums[:]:
        #     if i == val:
        #         nums.remove(i)
        # return len(nums)
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=val:
               nums[slow]=nums[fast]
               slow+=1
        return len(nums[:slow])

        