class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        boughtAt = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if (boughtAt > prices[i]):
                boughtAt = prices[i]
            elif (prices[i] - boughtAt > profit):
                profit = prices[i] - boughtAt
            
            
        
        return profit

