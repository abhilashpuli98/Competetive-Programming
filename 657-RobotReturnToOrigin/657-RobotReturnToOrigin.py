# Last Updated: 5/15/2026, 11:15:27 PM
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) & 1: return False
        f = Counter(moves)
        return f['U'] == f['D'] and f['L'] == f['R']