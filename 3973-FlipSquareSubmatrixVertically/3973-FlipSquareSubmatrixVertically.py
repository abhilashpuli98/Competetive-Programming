# Last Updated: 5/15/2026, 11:09:34 PM
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        sc,ec=y,y+k-1
        sr=x
        for i in range(sc,ec+1):
            for j in range(k//2):
                grid[sr+j][i],grid[sr+k-j-1][i]=grid[sr+k-j-1][i], grid[sr+j][i]
        return grid