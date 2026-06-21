# Last Updated: 6/22/2026, 12:44:28 AM
class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(mat),len(mat[0])
        col0=1
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    mat[i][0]=0
                    if j!=0:
                        mat[0][j]=0
                    else:
                        col0=0
        for i in range(1,m):
            for j in range(1,n):
                if mat[i][j]!=0 and (not mat[i][0] or not mat[0][j]):
                    mat[i][j]=0
        if not mat[0][0]:
            for i in range(n):
                mat[0][i]=0
        if not col0:
            for i in range(m):
                mat[i][0]=0
