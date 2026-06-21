# Last Updated: 6/22/2026, 12:42:25 AM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]