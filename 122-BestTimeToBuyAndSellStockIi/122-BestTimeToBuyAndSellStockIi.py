# Last Updated: 6/22/2026, 12:43:45 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:   
        maxi=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxi+=prices[i]-prices[i-1]
        return maxi