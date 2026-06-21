# Last Updated: 6/22/2026, 12:43:05 AM
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber>0:
            columnNumber-=1
            result.append(chr(columnNumber%26+ord('A')))
            columnNumber//=26
        return "".join(result[::-1])