# Last Updated: 5/15/2026, 11:10:45 PM
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n=len(nums)
        r=sorted(nums[1:])
        return r[0]+r[1]+nums[0]
        