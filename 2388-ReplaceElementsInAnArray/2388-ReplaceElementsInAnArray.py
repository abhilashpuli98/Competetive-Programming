# Last Updated: 5/15/2026, 11:11:34 PM
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mapper={}
        for i in range(len(nums)):
            mapper[nums[i]]=i
        for c,r in operations:
            nums[mapper[c]]=r
            mapper[r] = mapper[c]
        return nums