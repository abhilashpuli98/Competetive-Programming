# Last Updated: 6/22/2026, 12:41:37 AM
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0 and 3**19%n==0