# Last Updated: 6/22/2026, 12:41:45 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        for right in range(1,len(nums)):
            if nums[left]!=0:
                left+=1
            elif nums[left]==0 and nums[right]!=0:
                nums[right],nums[left]=nums[left],nums[right]
                left+=1
