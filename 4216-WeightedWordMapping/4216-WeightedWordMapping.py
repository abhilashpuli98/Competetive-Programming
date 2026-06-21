# Last Updated: 6/21/2026, 7:01:48 PM
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        i=0
        res=""
        for word in words:
            res+=(
                chr(
                    ord('z')-(
                        sum(weights[ord(char)-ord('a')] for char in word)%26
                        )
                    )
                )

            i+=len(word)
        return res
