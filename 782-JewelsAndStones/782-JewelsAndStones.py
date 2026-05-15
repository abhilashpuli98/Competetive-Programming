# Last Updated: 5/15/2026, 11:15:10 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for c in stones:
            if c in jewels:
                count+=1
        return count