# Last Updated: 5/15/2026, 11:12:15 PM
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        low=0
        high=len(mat[0])-1
        n=len(mat)
        m=len(mat[0])
        while low<=high:
            mid=(low+high)//2
            max_row=0
            for i in range(n):
                if mat[i][mid]>mat[max_row][mid]:
                    max_row=i
            left=-1 if mid-1<0 else mat[max_row][mid-1]
            right=-1 if mid+1>=m else mat[max_row][mid+1]
            if left<mat[max_row][mid] and mat[max_row][mid]>right:
                return [max_row,mid]
            if left>mat[max_row][mid]:
                high=mid-1
            else:
                low=mid+1