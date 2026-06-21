# Last Updated: 6/22/2026, 12:42:46 AM
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n>0:
            n=n&(n-1)
            count+=1
        return count