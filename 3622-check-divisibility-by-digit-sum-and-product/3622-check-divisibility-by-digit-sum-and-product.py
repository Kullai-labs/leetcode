class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ans=0
        prod=1
        # num=n
        # while n > 0:
        #     temp=n%10
        #     ans+=temp
        #     prod*=temp
        #     n//=10
        # if num % (ans+prod)==0:
        #     return True
        # return False
        n=str(n)
        for i in n:
            prod*=int(i)
            ans+=int(i)
        if int(n)%(ans+prod)==0:
            return True
        return False