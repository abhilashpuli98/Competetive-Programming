# Last Updated: 6/22/2026, 12:45:12 AM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        for right in range(1,len(nums)):
            if nums[left]!=nums[right]:
                left+=1
                nums[left]=nums[right]
            #right+=1
        return left+1
