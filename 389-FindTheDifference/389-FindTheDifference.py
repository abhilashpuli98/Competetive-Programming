# Last Updated: 6/21/2026, 7:06:43 PM
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result=0
        for letter in s:
            result^=(ord(letter))
        for letter in t:
            result^=(ord(letter))
        return chr(result)
        