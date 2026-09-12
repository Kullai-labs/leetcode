class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # left=0
        # max_sum=float('-inf')
        # window_sum=0
        # for right in range(len(nums)):
        #     window_sum+=nums[right]
        #     if right-left+1 == k:
        #         # avg1=window_sum/k
        #         max_sum=max(window_sum,max_sum)
        #         window_sum-=nums[left]
        #         left+=1
        # return max_sum/k
        # window_sum = sum(nums[:k])     
        # max_sum = window_sum
        # for right in range(k, len(nums)):
        #     window_sum += nums[right] - nums[right - k]  
        #     max_sum = max(max_sum, window_sum)
        # return max_sum / k 
        # if len(nums)<1:
        #     return -1
        left=0
        ans=float('-inf')
        sum1=0
        for right in range(len(nums)):
            sum1+=nums[right]
            if (right-left+1)==k:
                # avg1=(sum1)/k
                ans=max(ans,sum1)
                sum1-=nums[left]
                left+=1
        return ans/k

    
        