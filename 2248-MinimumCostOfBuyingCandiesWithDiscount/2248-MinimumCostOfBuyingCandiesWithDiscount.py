# Last Updated: 6/21/2026, 7:03:43 PM
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        res=0
        i=len(cost)-1
        while i>=0:
            res+=cost[i]
            if i-1>=0:
                res+=cost[i-1]
            i-=3
        return res