class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        for i in range(len(prices) - 1):
            j = i + 1
            if (prices[i] < prices[j]):
                # should buy
                prof += prices[j] - prices[i]
            
        return prof

