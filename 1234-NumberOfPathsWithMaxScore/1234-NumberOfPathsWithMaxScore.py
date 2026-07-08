# Last Updated: 7/9/2026, 12:18:43 AM
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD=10**9+7
        n=len(board)
        m=len(board[0])
        dp=[[(-1,0) for _ in range(n)] for _ in range(m)]
        dp[n-1][m-1]=(0,1)
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if board[i][j]=='X' or (i==m-1 and j==n-1):
                    continue
                best_score=-1
                ways=0
                for x,y in [(1,0),(0,1),(1,1)]:
                    nx,ny=i+x,y+j
                    if not (0<=nx<n and 0<=ny<m):
                        continue
                    score,cnt=dp[nx][ny]
                    if score==-1:
                        continue
                    if score>best_score:
                        best_score=score
                        ways=cnt
                    elif score==best_score:
                        ways=(ways+cnt)%MOD
                if best_score==-1:
                    continue
                val=0 if board[i][j] in 'ES' else int(board[i][j])
                dp[i][j]=(best_score+val,ways)
        score,ways=dp[0][0]
        if score==-1:
            return [0,0]
        else:
            return [score,ways]
