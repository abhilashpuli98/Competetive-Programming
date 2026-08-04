# Last Updated: 8/5/2026, 12:31:17 AM
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]          
        for char in s:
            if stack and stack[-1][0]==char:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            elif not stack or stack[-1][0]!=char:
                stack.append([char,1])
        return ''.join(char*c for char,c in stack)
