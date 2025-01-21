class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        profit =0 
        for r in range(len(prices)):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]+profit
            l=r
            r=r+1
        return profit
        
        
        