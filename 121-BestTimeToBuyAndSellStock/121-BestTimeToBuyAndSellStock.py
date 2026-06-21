# Last Updated: 6/22/2026, 12:43:46 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxi=0
        for price in prices:
            maxi=max(maxi,price-mini)
            mini=min(mini,price)
        return maxi