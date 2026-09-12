class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left=0 
        ans=0
        seen=set()
        total=0
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                total-=nums[left]
                left+=1
            seen.add(nums[right])
            total+=nums[right]

            if right-left+1 == k:
                # sum1=set(nums)
                # if len(sum1) == k:
                ans=max(ans,total)
                seen.remove(nums[left])
                total-=nums[left]
                left+=1
        return ans


        