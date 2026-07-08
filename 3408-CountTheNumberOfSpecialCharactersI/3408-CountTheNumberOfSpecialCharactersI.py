# Last Updated: 7/9/2026, 12:18:02 AM
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower=set()
        upper=set()
        count=0
        for char in word:
            if char.islower():
                lower.add(char)
            else:
                upper.add(char)
        for char in lower:
            if char.upper() in upper:
                count+=1
        return count
            