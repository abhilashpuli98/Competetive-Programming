# Last Updated: 5/15/2026, 11:15:04 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        s=s+s
        return goal in s