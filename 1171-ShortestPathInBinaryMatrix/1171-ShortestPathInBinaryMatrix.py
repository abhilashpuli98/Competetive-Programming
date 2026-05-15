# Last Updated: 5/15/2026, 11:13:57 PM
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        visited=set()
        visited.add((0,0))
        q=deque([(1,0,0)])
        dirs=[
            [1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]
        ]
        n=len(grid)
        m=len(grid[0])
        while q:
            dist,row,col=q.popleft()
            if row==n-1 and col==m-1:
                return dist
            for x,y in dirs:
                x,y=x+row,col+y
                if min(x,y)>=0 and max(x,y)<n and grid[x][y]!=1 and (x,y) not in visited:
                    q.append((dist+1,x,y))
                    visited.add((x,y))
        return -1

