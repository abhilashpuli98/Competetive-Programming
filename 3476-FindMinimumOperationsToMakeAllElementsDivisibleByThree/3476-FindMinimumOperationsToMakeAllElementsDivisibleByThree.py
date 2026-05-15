# Last Updated: 5/15/2026, 11:10:31 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum([1 for val in nums if val%3!=0])
