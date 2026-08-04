# Last Updated: 8/5/2026, 12:31:04 AM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fm,sm=0,0
        for i in range(len(nums)):
            if fm<nums[i]:
                if fm >sm:
                    sm=fm
                fm=nums[i]
            elif fm>=nums[i] and sm<nums[i]:
                sm=nums[i]
        return (fm-1)*(sm-1)