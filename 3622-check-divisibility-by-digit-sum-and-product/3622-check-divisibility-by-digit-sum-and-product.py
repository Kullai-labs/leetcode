class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ans=0
        prod=1
        num=n
        while n > 0:
            temp=n%10
            ans+=temp
            prod*=temp
            n//=10
        # / num % ans and num % prod
        # if ans or prod is 0:
        #     return False
        if num % (ans+prod)==0:
            return True
        return False
       