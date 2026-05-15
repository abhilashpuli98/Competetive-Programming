# Last Updated: 5/15/2026, 11:15:05 PM
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        minheap=[]
        dirs=[[1,0],[0,1],[-1,0],[0,-1]]
        heapq.heappush(minheap,[grid[0][0],0,0])
        visited=set()
        while minheap:
            time,row,col=heapq.heappop(minheap)
            if row==n-1 and col==n-1:
                return time
            for r,c in dirs:
                nr,nc=row+r,col+c
                if nr<0 or nr==n or nc<0 or nc==n or (nr,nc) in visited:
                    continue
                heapq.heappush(minheap,[max(time,grid[nr][nc]),nr,nc])
                visited.add((nr,nc))