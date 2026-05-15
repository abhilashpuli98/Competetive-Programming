# Last Updated: 5/15/2026, 11:14:06 PM
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq=[0]*26
        result=0
        flag=1
        for char in chars:
            freq[ord(char)-ord('a')]+=1
        for word in words:
            count=[0]*26
            for char in word:
                count[ord(char)-ord('a')]+=1
            for i in range(26):
                if count[i]>freq[i]:
                    flag=0
                    break
                elif count[i]<=freq[i]:
                    flag=1
            if flag!=0:
                result+=len(word)
            flag=1
        return result

