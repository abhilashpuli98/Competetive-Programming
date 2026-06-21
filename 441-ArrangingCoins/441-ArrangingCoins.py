# Last Updated: 6/21/2026, 7:06:27 PM
class Solution:
    def arrangeCoins(self, n: int) -> int:
        total=0
        i=1
        while n:
            if n>=i:
                total+=1
                n-=i
                i+=1
            else:
                return total
        return total
