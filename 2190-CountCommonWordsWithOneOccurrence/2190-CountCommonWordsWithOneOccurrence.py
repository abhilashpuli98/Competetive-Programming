# Last Updated: 5/15/2026, 11:11:57 PM
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1=Counter(words1)
        c2=Counter(words2)
        count=0
        """common=set(words1).intersection(set(words2))
        for item in common:
            if c1[item]==1 and c2[item]==1:
                count+=1"""
        for key in c1.keys():
            if c1[key]==1 and c2[key]==1:
                count+=1
        return count