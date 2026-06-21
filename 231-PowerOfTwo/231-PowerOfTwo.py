# Last Updated: 6/22/2026, 12:42:07 AM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and not n&(n-1)