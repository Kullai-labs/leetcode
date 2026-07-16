
class Solution(object):
    def gcdSum(self, nums):

        def gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        pre=[]
        mx= nums[0]
        for i in nums:
            mx=max(mx,i)
            pre.append(gcd(mx,i))
        pre.sort()
        total_sum = 0
        l=0
        r=len(pre)-1
        while l<r:
            total_sum+=gcd(pre[l],pre[r])
            l+=1
            r-=1
          
        return total_sum

        
        