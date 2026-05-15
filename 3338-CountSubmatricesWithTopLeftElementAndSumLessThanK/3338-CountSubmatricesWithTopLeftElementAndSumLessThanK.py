# Last Updated: 5/15/2026, 11:10:42 PM
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        grid = map(accumulate,zip(*map(accumulate,grid)))
        return sum(val<=k for row in grid for val in row)