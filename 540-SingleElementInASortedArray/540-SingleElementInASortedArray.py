# Last Updated: 5/15/2026, 11:15:50 PM
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1 or nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        low,high=1,len(nums)-2
        while low<=high:
            mid=(low+high)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if (mid%2==0 and nums[mid+1]==nums[mid]) or (mid%2!=0 and nums[mid-1]==nums[mid]):
                low=mid+1
            else:
                high=mid-1
                