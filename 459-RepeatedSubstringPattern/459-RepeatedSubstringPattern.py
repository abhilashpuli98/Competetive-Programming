# Last Updated: 6/21/2026, 7:06:17 PM
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]