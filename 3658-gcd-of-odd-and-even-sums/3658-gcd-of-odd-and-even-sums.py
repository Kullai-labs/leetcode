class Solution(object):
    def gcdOfOddEvenSums(self, n):
        e=n*(n+1)
        o=n*n
        # while o:
        #     e,o=o,e%o
        # return e
        # return n
        def gcd(e,o):
            if o==0:
                return e
            else:
                return gcd(o,e%o)
        return gcd(e,o)
        
       
        