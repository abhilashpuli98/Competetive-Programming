# Last Updated: 5/15/2026, 11:13:19 PM
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])-1,-1,-1):
                if grid[i][j]>=0:
                    count+=(len(grid[i])-(j+1))
                    break
            else:
                count+=len(grid[i])
        return count