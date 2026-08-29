class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result=[]
        balence=0
        for ch in s:
            if ch == '(':
                if balence> 0:
                    result.append(ch)
                balence+=1
            else:
                balence-=1
                if balence>0:
                    result.append(ch)
        return ''.join(result)
             
        
        