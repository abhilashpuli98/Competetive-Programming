# Last Updated: 6/21/2026, 7:04:46 PM
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x : x[0]-x[1])
        n=len(costs)
        cost1=0
        cost2=0
        for i in range(n//2):
            cost1+=costs[i][0]
        for i in range(n//2,n):
            cost2+=costs[i][1]
        return cost1+cost2
