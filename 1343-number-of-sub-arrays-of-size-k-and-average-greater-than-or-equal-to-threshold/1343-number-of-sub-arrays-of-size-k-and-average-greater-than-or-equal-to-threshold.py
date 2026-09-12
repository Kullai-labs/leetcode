class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, t: int) -> int:
        # target = k * t
        # count=0
        # window_sum=sum(arr[:k])
        # # if (window_sum)>=target:
        # #     count+=1
        # count=1 if window_sum >=target else 0
        # for right in range(k,len(arr)):
        #     window_sum+=arr[right]-arr[right-k]
        #     if (window_sum)>=target:
        #         count+=1
        # return count
        sum1=0
        c=0
        left=0
        for right in range(len(nums)):
            sum1+=nums[right]
            if (right-left+1)==k:
                if sum1/k >= t:
                    c+=1
                sum1-=nums[left]
                left+=1
        return c
        


         
