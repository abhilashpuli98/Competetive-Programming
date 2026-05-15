# Last Updated: 5/15/2026, 11:10:57 PM
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left_mini=[float('inf')]*n
        right_mini=[float('inf')]*n

        m=nums[0]
        for i in range(1,n):
            left_mini[i]=m
            m=min(m,nums[i])
        m=nums[-1]
        for i in range(n-2,-1,-1):
            right_mini[i]=m
            m=min(m,nums[i])
        res=float('inf')
        for j in range(1,n-1):
            if left_mini[j]<nums[j] and right_mini[j]<nums[j]:
                res=min(res,left_mini[j]+nums[j]+right_mini[j])
        return res if res!=float('inf') else -1


