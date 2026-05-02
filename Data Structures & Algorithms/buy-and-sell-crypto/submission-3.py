class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minPrice = prices[0]
        
        for i in range(len(prices)):
            currPro = prices[i] - minPrice
            maxPro = max(currPro, maxPro)
            minPrice = min(minPrice, prices[i])
            
        return maxPro