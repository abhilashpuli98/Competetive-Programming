# Last Updated: 5/15/2026, 11:12:42 PM
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        biRep=""
        for i in range(1,n+1):
            biRep+=bin(i)[2:]
        return (int(biRep,2))%(10**9+7)
