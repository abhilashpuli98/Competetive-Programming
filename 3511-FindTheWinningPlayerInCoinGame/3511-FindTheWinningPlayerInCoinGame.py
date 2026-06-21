# Last Updated: 6/21/2026, 7:02:20 PM
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        count=0
        while x>0 and y>3:
            x-=1
            y-=4
            count+=1
        return 'Bob' if not count%2 else 'Alice'