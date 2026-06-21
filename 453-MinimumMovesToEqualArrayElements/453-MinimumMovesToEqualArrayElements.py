# Last Updated: 6/21/2026, 7:06:20 PM
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-min(nums)*len(nums)