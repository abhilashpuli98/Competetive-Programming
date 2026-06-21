# Last Updated: 6/22/2026, 12:44:52 AM
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
            return list(set(list(itertools.permutations(nums))))