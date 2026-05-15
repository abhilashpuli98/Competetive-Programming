# Last Updated: 5/15/2026, 11:12:49 PM
class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        maxi=0
        for char in s:
            if char=='(':
                depth+=1
                maxi=max(maxi,depth)
            if char==")":
                depth-=1       
        return maxi