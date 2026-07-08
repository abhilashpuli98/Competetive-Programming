# Last Updated: 7/9/2026, 12:17:59 AM
class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]
        def backtracker(s):
            if len(s)==n:
                ans.append(s)
                return
            if not s or s[-1]!='0':
                backtracker(s+'0')
            backtracker(s+'1')
        backtracker("")
        return ans

        