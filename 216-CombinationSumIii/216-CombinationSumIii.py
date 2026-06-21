# Last Updated: 6/22/2026, 12:42:24 AM
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path=[]
        res=[]
        def backtracker(i,sum,count):
            if sum==0 and count==0:
                res.append(path[:])
                return
            if count<=0 or sum<0:
                return
            for x in range(i,10):
                path.append(x)
                backtracker(x+1,sum-x,count-1)
                path.pop()
        backtracker(1,n,k)
        return res
