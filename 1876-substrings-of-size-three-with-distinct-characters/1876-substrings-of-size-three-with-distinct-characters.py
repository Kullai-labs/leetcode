class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # ans=0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         temp=[]
        #         for k in range(i,j+1):
        #             temp.append(s[k])
        #         if len(temp)==3 and len(set(temp))==3:
        #             ans+=1
        # return ans/
        count=0
        for i in range(len(s)-2):
            ch_1=s[i]
            ch_2=s[i+1]
            ch_3=s[i+2]
            if ch_1!=ch_2 and ch_1!=ch_3 and ch_2!=ch_3:
                count+=1
        return count
        