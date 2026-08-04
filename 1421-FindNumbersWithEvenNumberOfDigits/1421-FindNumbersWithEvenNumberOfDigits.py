# Last Updated: 8/5/2026, 12:31:13 AM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            x=len(str(num))
            if not x%2:
                count+=1
        return count