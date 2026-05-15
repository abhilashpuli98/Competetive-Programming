# Last Updated: 5/15/2026, 11:13:09 PM
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        comb=set()
        for i in range(len(s)-k+1):
            comb.add(s[i:i+k])
        return len(comb)==2**k