class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor=0
        # for i in nums:
        #     xor^=i
        # return xor
        ans={}
        for num in nums:
            if num in ans:
                ans[num]+=1
            else:
                ans[num]=1
        for key in ans:
            if ans[key]==1:
                return key
            
        
