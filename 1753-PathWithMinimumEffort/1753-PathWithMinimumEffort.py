# Last Updated: 8/5/2026, 12:30:52 AM
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        eff=[[float('inf')]*n for _ in range(m)]
        pq=[]
        eff[0][0]=0
        dirs=[[1,0],[0,1],[-1,0],[0,-1]]
        heapq.heappush(pq,(0,0,0))
        while pq:
            d,i,j=heapq.heappop(pq)
            if d>eff[i][j]:
                continue
            for dx,dy in dirs:
                nx,ny=i+dx,j+dy
                if 0<=nx<m and 0<=ny<n:
                    curr_effort=abs(heights[i][j]-heights[nx][ny])
                    max_effort=max(d,curr_effort)
                    if eff[nx][ny]>max_effort:
                        eff[nx][ny]=max_effort
                        heapq.heappush(pq,(max_effort,nx,ny))
        return eff[-1][-1]                             