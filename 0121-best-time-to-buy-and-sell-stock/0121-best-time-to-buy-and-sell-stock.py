class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr=0
        maximum=0
        for i in range(1,len(prices)):
            diff=prices[i]-prices[i-1]
            curr=max(diff,curr+diff)
            maximum=max(maximum,curr)
        return maximum
        