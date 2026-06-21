# Last Updated: 6/22/2026, 12:45:02 AM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """low=0
        high=len(nums)-1
        ans=len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans"""
        return bisect.bisect_left(nums,target)