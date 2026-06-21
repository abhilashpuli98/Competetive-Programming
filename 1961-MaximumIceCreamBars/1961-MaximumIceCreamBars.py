# Last Updated: 6/22/2026, 12:40:40 AM
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        for cost in costs:
            if cost>coins:
                return count
            coins-=cost
            count+=1
        return count