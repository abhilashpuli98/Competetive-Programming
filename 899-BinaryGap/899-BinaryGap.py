# Last Updated: 5/15/2026, 11:14:48 PM
class Solution:
    def binaryGap(self, n: int) -> int:
        binary=bin(n)[2:]
        maxi=0
        left=0
        for i in range(1,len(binary)):
            if binary[i]=='1':
                maxi=max(maxi,abs(left-i))
                left=i
        return maxi 
