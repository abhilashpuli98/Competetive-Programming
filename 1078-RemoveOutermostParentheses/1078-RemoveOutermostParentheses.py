# Last Updated: 5/15/2026, 11:14:11 PM
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        opened=0
        for para in s:
            if para=='(' and opened>0:
                res+='('
            if para==')' and opened>1:
                res+=')'
            opened+=1 if para=='(' else -1
        return res

