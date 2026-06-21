# Last Updated: 6/22/2026, 12:44:32 AM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]