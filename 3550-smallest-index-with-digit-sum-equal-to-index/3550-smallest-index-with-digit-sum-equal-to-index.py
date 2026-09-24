class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            s=sum(int(i) for i in str(n))   
            if i==s:
                return i
            

        return -1

        