class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen={}
        for n in nums:
            seen[n]=seen.get(n,0)+1
            # if n in seen:
            #     seen[n]+=1
            # seen+=n
        # for i ,j in seen.items:
        #     return max(j)
        
        return max(seen,key=seen.get)