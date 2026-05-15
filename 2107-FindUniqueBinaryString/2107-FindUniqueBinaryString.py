# Last Updated: 5/15/2026, 11:12:04 PM
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join('0' if nums[i][i]=='1' else '1' for i in range(len(nums)))