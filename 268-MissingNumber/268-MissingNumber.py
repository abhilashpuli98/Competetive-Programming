# Last Updated: 6/22/2026, 12:41:50 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result=len(nums)
        for i in range(len(nums)):
                result^=nums[i]^i
        return result