# Last Updated: 6/21/2026, 7:05:12 PM
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count=0
        m=len(grid)
        n=len(grid[0])
        def isValid(i,j,k):
            if set(
                grid[r][c]
                for r in range(i,i+3)
                for c in range(j,j+3)
            ) != set(range(1,10)):
                return False
            target=None
            for x in range(i,i+k):
                row=sum(grid[x][j:j+k])
                if target is None:
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
        for i in range(m-3+1):
            for j in range(n-3+1):
                if isValid(i,j,3):
                    count+=1
        return count