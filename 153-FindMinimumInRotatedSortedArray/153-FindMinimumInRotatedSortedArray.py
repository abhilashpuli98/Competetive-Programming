# Last Updated: 6/22/2026, 12:43:11 AM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        mini=float('inf')
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:
                mini=min(mini,nums[low])
                low=mid+1
            else:
                mini=min(mini,nums[mid])
                high=mid-1
        return mini