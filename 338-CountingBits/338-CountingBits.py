# Last Updated: 6/21/2026, 7:06:57 PM
class Solution:
    def countBits(self, n: int) -> List[int]:
        def counter(num):
            count=0
            for i in range(32):
                if (num>>i)&1:
                    count+=1
            return count
        return [counter(i) for i in range(n+1)]