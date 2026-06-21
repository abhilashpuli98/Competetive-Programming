# Last Updated: 6/21/2026, 7:06:15 PM
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x=x^y
        return x.bit_count()