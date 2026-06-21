# Last Updated: 6/22/2026, 12:45:03 AM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i=bisect.bisect_left(nums,target)
        if i==len(nums) or nums[i]!=target:
            return [-1,-1]
        return [i,bisect.bisect_right(nums,target)-1]