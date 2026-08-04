# Last Updated: 8/5/2026, 12:31:18 AM
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        res=1
        m=len(grid)
        n=len(grid[0])
        def isValid(i,j,k):
            target=None
            for x in range(i,i+k):
                row=sum(grid[x][j:j+k])
                if not target:
                    target=row
                elif target!=row:
                    return False
            for col in range(j,j+k):
                if sum(grid[r][col] for r in range(i,i+k))!=target:
                    return False
            if sum(grid[i+d][j+d] for d in range(k))!=target:
                return False
            if sum(grid[i+d][j+k-d-1] for d in range(k))!=target:
                return False
            return True
        for k in range(min(m,n),1,-1):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    if isValid(i,j,k):
                        return k
        return 1