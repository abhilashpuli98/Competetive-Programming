# Last Updated: 6/21/2026, 7:05:08 PM
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])
        res=[]
        for i in range(m):
            temp=[]
            for j in range(n):
                temp.append(matrix[j][i])
            res.append(temp)
        return res