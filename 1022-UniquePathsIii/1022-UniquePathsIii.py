# Last Updated: 6/21/2026, 7:04:56 PM
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def backtracker(i,j,c):
            if not (0<=i<r) or not(0<=j<col) or grid[i][j]==-1:
                return 0
            if grid[i][j]==2:
                if c==count:
                    return 1
                return 0
            temp=grid[i][j]
            grid[i][j]=-1
            ans=0
            ans+=backtracker(i+1,j,c+1)+backtracker(i-1,j,c+1)+backtracker(i,j+1,c+1)+backtracker(i,j-1,c+1)
            grid[i][j]=temp
            return ans

        r=len(grid)
        col=len(grid[0])
        sr,sc=0,0
        count=0
        for i in range(r):
            for j in range(col):
                if grid[i][j]==1:
                    sr,sc=i,j
                if grid[i][j]!=-1:
                    count+=1
        return backtracker(sr,sc,1)

