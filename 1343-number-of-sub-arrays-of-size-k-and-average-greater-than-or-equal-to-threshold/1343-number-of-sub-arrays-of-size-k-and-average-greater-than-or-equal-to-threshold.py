class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        target = k * t
        count=0
        window_sum=sum(arr[:k])
        # if (window_sum)>=target:
        #     count+=1
        count=1 if window_sum >=target else 0
        for right in range(k,len(arr)):
            window_sum+=arr[right]-arr[right-k]
            if (window_sum)>=target:
                count+=1
        return count

         
