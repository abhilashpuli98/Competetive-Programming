# Last Updated: 6/22/2026, 12:43:34 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            res^=num
        return res