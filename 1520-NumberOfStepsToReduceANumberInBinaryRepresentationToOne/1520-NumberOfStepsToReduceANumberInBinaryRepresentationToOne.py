# Last Updated: 5/15/2026, 11:13:13 PM
class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        """ anog
        1 0 1 0 0
        16 8 4 2 1 ==> 20
        0 1 0 1 0
        1 1 1 1 0 => 30
        0 1 1 1 1
        #adding 1 leds to cary '1' to right to left(lsb-msb)
        #division led to shift in all bins to Left to right(msb-lsb)
        """
        for i in range(len(s)-1,0,-1):
            lsbit = int(s[i])+carry
            if lsbit == 1:
                carry = 1
                steps+=2
            else:
                steps+=1
        return steps+carry 