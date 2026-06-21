# Last Updated: 6/22/2026, 12:43:50 AM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        res=[[1]]
        for i in range(1,numRows):
            prev=res[-1]
            curr=[1]
            for j in range(1,len(prev)):
                curr.append(prev[j-1]+prev[j])
            curr.append(1)
            res.append(curr)
        return res
