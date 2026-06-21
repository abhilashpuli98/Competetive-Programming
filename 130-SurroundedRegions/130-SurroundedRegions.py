# Last Updated: 6/22/2026, 12:43:39 AM
class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(grid)
        n=len(grid[0])
        def dfs(r,c):
            if not (0<=r<m) or not(0<=c<n) or grid[r][c]!='O':
                return
            grid[r][c]='A'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for r in range(m):
            if grid[r][0]=='O':
                dfs(r,0)
            if grid[r][n-1]=='O':
                dfs(r,n-1)
        for c in range(n):
            if grid[0][c]=='O':
                dfs(0,c)
            if grid[m-1][c]=='O':
                dfs(m-1,c)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='A':
                    grid[i][j]='O'
                elif grid[i][j]=='O':
                    grid[i][j]='X'
            
