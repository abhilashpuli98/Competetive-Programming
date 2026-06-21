# Last Updated: 6/21/2026, 7:06:39 PM
class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen=set()
        leng=0
        for c in s:
            if c in seen:
                seen.remove(c)
                leng+=2
            else:
                seen.add(c)
        return leng+1 if seen else leng