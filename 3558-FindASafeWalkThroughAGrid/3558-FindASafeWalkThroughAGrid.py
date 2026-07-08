# Last Updated: 7/9/2026, 12:17:54 AM
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m=len(grid)
        n=len(grid[0])
        initial_health=health-grid[0][0]
        if initial_health<=0:
            return False
        q=deque([(0,0,initial_health)])
        best=[[-1]*n for _ in range(m)]
        best[0][0]=initial_health
        while q:
            i,j,h=q.popleft()
            if i==m-1 and j==n-1 and h>=1:
                return True
            for x,y in [(1,0),(0,1),(0,-1),(-1,0)]:
                nx,ny=i+x,j+y
                if not(0<=nx<m and 0<=ny<n) or (grid[nx][ny]==1 and h-1<=0):
                    continue
                b=h if grid[nx][ny]==0 else h-1
                if best[nx][ny]>=b:
                    continue
                best[nx][ny]=b
                q.append((nx,ny, b))
        return False
