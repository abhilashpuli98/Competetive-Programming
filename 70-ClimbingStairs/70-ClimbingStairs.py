# Last Updated: 6/22/2026, 12:44:29 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        res=[2,3]
        for i in range(4,n+1):
            res[0],res[1]=res[1],(res[0]+res[1])
        return res[-1]