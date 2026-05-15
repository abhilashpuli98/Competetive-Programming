# Last Updated: 5/15/2026, 11:09:54 PM
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if all(n<0 for n in nums):
            return max(nums)
        return sum([x for x in set(nums) if x>=0])