# Last Updated: 5/15/2026, 11:10:11 PM
class Solution:
    def smallestNumber(self, n: int) -> int:
        while True:
            bi=str(bin(n))[2:]
            if '0' not in bi:
                return n
            else:
                n+=1
