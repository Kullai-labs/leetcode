class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # for i in range(len(k)):
        #     s[i],s[i+1]=s[i+1],s[i]
        # return s
        ans=s[:k:]
        r=ans[::-1]
        return  r+s[k:]
        