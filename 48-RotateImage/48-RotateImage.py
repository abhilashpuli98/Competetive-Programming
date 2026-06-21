# Last Updated: 6/22/2026, 12:44:50 AM
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i<j:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            p=0
            q=len(matrix[i])-1
            while p<=q:
                matrix[i][p],matrix[i][q]=matrix[i][q],matrix[i][p]
                p+=1
                q-=1
            

        