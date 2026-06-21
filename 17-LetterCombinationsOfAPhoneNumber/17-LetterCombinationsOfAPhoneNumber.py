# Last Updated: 6/22/2026, 12:45:22 AM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lett_dict={
            '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
        n=len(digits)
        res=[]
        def backtracker(i,string):
            if len(string)==n:
                res.append(string)
                return
            for char in lett_dict[digits[i]]:
                backtracker(i+1,string+char)
        backtracker(0,"")
        return res