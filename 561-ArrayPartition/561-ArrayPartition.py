# Last Updated: 5/15/2026, 11:15:43 PM
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])