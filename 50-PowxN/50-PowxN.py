# Last Updated: 6/22/2026, 12:44:47 AM
class Solution:
    def myPow(self, num: float, n: int) -> float:
        def helper(x,p):
            if x==0:
                return 0
            if p==0:
                return 1
            res=helper(x,p//2)
            res*=res
            if p%2:
                return res*x
            return res
        res=helper(num,abs(n))
        if n<0:
            return 1/res
        return res