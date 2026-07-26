class Solution:
    def maxProduct(self, n: int) -> int:
        # n=str(n)
        # ans=1
        # max1=1
        # for i in n:
        #     ans*=int(i)
        #     max1=max(max1,ans)
        # return ans
        nums=list(str(n))
        nums.sort()
        return int(nums[-1])*int(nums[-2])

        