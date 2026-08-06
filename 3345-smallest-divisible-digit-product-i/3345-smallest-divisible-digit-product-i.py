class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        current = n
        product=1
        while n > 0 :
            temp=n%10
            product*=temp
            n=n//10
        if product % t==0:
            return current
        else:
            return self.smallestNumber(current+1,t)


        