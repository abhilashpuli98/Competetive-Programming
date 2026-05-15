# Last Updated: 5/15/2026, 11:12:31 PM
class Solution:
    def minOperations(self, s: str) -> int:
        flipCount1,flipCount2=0,0
        for i in range(len(s)):
            if s[i]==('0' if i%2==0 else '1'):
                flipCount1+=1
            if s[i]==('1' if i%2==0 else '0'):
                flipCount2+=1
        return min(flipCount1,flipCount2)
    