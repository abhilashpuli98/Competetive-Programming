# Last Updated: 7/9/2026, 12:18:49 AM
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for char in s:
            if not stack:
                stack.append(char)
            elif stack[-1]==char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
