# Last Updated: 5/15/2026, 11:13:14 PM
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res=[]
        total=3*(2**(n-1))
        left,right=1,total
        choices='abc'
        for _ in range(n):
            curr=left
            partition_size = (right-left+1)//len(choices)
            for ch in choices:
                if k in range(curr,curr+partition_size):
                    res.append(ch)
                    left=curr
                    right=curr+partition_size-1
                    choices='abc'.replace(ch,"")
                    break
                curr+=partition_size
        return "".join(res)