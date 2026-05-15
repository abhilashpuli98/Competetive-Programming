# Last Updated: 5/15/2026, 11:15:25 PM
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n>>1)
        return x&(x+1)==0