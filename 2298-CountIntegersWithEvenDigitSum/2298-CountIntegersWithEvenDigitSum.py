# Last Updated: 6/21/2026, 7:03:39 PM
class Solution:
    def countEven(self, num: int) -> int:
    
        return sum(
            1  
            for i in range(1,num+1)
             if sum(int(char) for char in str(i))%2==0
            )