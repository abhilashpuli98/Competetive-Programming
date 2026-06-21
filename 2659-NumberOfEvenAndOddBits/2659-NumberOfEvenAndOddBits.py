# Last Updated: 6/21/2026, 7:03:18 PM
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        birep=bin(n)[2:]
        n=len(birep)
        even=0
        odd=0
        for i in range(len(birep)-1,-1,-1):
            if (n-i-1)%2==0 and birep[i]=='1':
                even+=1
            elif (n-i-1)%2==1 and birep[i]=='1':
                odd+=1
        return [even,odd]
            