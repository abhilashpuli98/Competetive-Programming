# Last Updated: 5/15/2026, 11:10:28 PM
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[[0,False] for _ in range(n)] for _ in range(m)]
        count=0
        vdict={'X':1,'Y':-1,'.':0}
        for i in range(m):
            for j in range(n):
                hasX=(grid[i][j]=='X')
                val=vdict[grid[i][j]]
                top_sum = dp[i-1][j][0] if i>0 else 0
                left_sum = dp[i][j-1][0] if j>0 else 0
                diag_sum=dp[i-1][j-1][0] if i>0 and j>0 else 0
                dp[i][j][0]=top_sum+left_sum-diag_sum+val

                top_flag = dp[i-1][j][1] if i>0 else False
                left_flag = dp[i][j-1][1] if j>0 else False
                dp[i][j][1]=left_flag or top_flag or hasX
                if dp[i][j][0]==0 and dp[i][j][1]:
                    count+=1
        return count