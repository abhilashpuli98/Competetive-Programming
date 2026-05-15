# Last Updated: 5/15/2026, 11:09:24 PM
class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return abs(sum(nums[:k])-sum(nums[-1:-k-1:-1]))