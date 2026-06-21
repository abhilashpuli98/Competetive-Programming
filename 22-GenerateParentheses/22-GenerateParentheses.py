# Last Updated: 6/22/2026, 12:45:15 AM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        curr=[]
        def backtracker(open,close):
            if len(curr)==2*n:
                res.append(''.join(curr))
                return
            if open<n:
                curr.append('(')
                backtracker(open+1,close)
                curr.pop()
            if close<open:
                curr.append(')')
                backtracker(open,close+1)
                curr.pop()
        backtracker(0,0)
        return res