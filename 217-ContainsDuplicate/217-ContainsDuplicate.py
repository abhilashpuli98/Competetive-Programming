# Last Updated: 6/22/2026, 12:42:23 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq=set()
        for i in range(len(nums)):
            if nums[i] in freq:
                return True
            else:
                freq.add(nums[i])
        return False
