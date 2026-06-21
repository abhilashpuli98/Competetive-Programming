# Last Updated: 6/21/2026, 7:04:12 PM
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        res=0
        for i in range(m):
            res+=mat[i][i]+mat[i][n-i-1]
        if n % 2 == 1:
            res-=mat[n // 2][n // 2]
        return res