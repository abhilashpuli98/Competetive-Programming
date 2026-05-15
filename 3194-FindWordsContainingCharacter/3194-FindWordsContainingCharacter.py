# Last Updated: 5/15/2026, 11:10:53 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i,word in enumerate(words) if x in word]