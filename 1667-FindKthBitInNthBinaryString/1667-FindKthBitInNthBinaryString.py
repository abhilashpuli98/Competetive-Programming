# Last Updated: 5/15/2026, 11:12:57 PM
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2**n-1
        invert = False

        while length>1:
            half = length//2
            if k<=half:
                length=half
            elif k>half+1:
                k=1+length-k
                length=half
                invert= not invert
                #return '1' if invert else '0'
            else:
                return '0' if invert else '1'
        return '1' if invert else '0'
