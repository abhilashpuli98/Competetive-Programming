# Last Updated: 5/15/2026, 11:15:23 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        left=0
        for i in range(len(nums)):
            right=total-left-nums[i]
            if right==left:
                return i
            left+=nums[i]
        return -1