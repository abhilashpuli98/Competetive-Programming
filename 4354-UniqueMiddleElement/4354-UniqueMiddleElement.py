# Last Updated: 7/9/2026, 12:17:21 AM
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid=len(nums)//2
        return True if nums.count(nums[mid])==1 else False