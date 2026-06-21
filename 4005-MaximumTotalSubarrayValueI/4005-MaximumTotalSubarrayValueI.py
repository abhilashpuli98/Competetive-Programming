# Last Updated: 6/21/2026, 7:01:55 PM
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k*(max(nums))-k*(min(nums))