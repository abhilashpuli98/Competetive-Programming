# Last Updated: 5/15/2026, 11:12:23 PM
class Solution:
    def rotate(self,mat):
        return [list(row) for row in zip(*mat[::-1])]
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat==target:
                return True
            mat = self.rotate(mat)
        return False