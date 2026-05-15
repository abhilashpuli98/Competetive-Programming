# Last Updated: 5/15/2026, 11:09:15 PM
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums+nums[::-1]