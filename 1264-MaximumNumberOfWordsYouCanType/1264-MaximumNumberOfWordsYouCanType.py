# Last Updated: 5/15/2026, 11:13:50 PM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words=text.split(" ")
        count=0
        for word in words:
            isrep=True
            for letter in brokenLetters:
                if letter in word:
                    isrep=False
            if isrep:
                count+=1
        return count