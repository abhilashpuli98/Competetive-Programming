# Last Updated: 5/15/2026, 11:11:41 PM
class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """

        xor_result = start ^ goal
        ans = 0
        
        while xor_result > 0:
            ans += xor_result & 1  
            xor_result >>= 1     
        
        return ans