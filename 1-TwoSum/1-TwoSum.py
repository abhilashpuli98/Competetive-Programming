# Last Updated: 6/22/2026, 12:45:45 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            difference = target-num
            if difference in seen:
                return [seen[difference],i]
            seen[num]=i 