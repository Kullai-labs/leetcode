class Solution(object):
    def isPerfectSquare(self, num):
        i=1
        while i*i <= num:
            i+=1
        return (i-1)*(i-1) == num

        