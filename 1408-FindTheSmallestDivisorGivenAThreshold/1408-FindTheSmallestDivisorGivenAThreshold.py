# Last Updated: 5/15/2026, 11:13:36 PM
class Solution:
    def isPossible(self,nums,t,d):
        total=0
        for x in nums:
            total+=ceil(x/d)
        return True if total<=t else False
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            if self.isPossible(nums,threshold,mid):
                high=mid-1
            else:
                low=mid+1
        return low