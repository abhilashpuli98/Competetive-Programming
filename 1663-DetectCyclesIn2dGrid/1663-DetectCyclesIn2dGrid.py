# Last Updated: 5/15/2026, 11:12:59 PM
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        dirs=[
            [1,0],[0,1],[-1,0],[0,-1]
        ]
        def dfs(i,j,pi,pj,letter):
            if not (0<=i<rows) or not(0<=j<cols) or grid[i][j]!=letter:
                return False
            if (i,j) in visited:
                return True
            visited.add((i,j))
            for x,y in dirs:
                nx,ny = i+x,j+y
                if pi==nx and ny==pj:
                    continue
                if dfs(nx,ny,i,j,letter):
                    return True
            return False
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited:
                    if  dfs(i,j,-1,-1,grid[i][j]):
                        return True
        return False
