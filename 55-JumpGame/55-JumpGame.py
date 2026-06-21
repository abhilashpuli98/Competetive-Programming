# Last Updated: 6/22/2026, 12:44:42 AM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0
        for i in range(len(nums)):
            if i>maxi:
                return False
            maxi=max(maxi,nums[i]+i)
        return True