# Last Updated: 6/22/2026, 12:45:32 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return  str(x)==str(x)[::-1]