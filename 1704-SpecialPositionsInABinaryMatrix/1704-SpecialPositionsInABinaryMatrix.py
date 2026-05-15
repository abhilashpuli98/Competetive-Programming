# Last Updated: 5/15/2026, 11:12:56 PM
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count=0
        cols=[0]*len(mat[0])
        rows=[0]*len(mat)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    rows[i]+=1
                    cols[j]+=1
        return sum(
            mat[i][j]==1 and rows[i]==1 and cols[j]==1
            for i in range(len(mat))
            for j in range(len(mat[0]))
        )