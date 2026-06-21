# Last Updated: 6/21/2026, 7:05:32 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(n):
            if n==0 or n==1:
                return 0
            if n in memo:
                return memo[n]
            memo[n]= min(cost[n-1]+helper(n-1),cost[n-2]+helper(n-2))
            return memo[n]
        memo={}
        n=len(cost)
        return helper(n)
        
        
        """cost.append(0)
        for i in range(len(cost)-4, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2]) 
        return min(cost[0], cost[1])"""