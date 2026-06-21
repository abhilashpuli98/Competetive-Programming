# Last Updated: 6/21/2026, 7:03:12 PM
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[0]*(n)
        sufix=[0]*(n)
        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i-1]
        for i in range(n-2,-1,-1):
            sufix[i]=sufix[i+1]+nums[i+1]
        res=[]
        for x,y in zip(prefix,sufix):
            res.append(abs(x-y))
        return res