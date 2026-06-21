# Last Updated: 6/21/2026, 7:05:37 PM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def dfs(i,j):
            if not(0<=i<m) or not(0<=j<n) or grid[i][j]!=1:
                return 0
            grid[i][j]=0
            return 1+(dfs(i+1,j)+
            dfs(i-1,j)+
            dfs(i,j+1)+
            dfs(i,j-1))
        area=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    area=max(area,dfs(i,j))
        return area