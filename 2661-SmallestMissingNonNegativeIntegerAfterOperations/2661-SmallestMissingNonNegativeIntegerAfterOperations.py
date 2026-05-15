# Last Updated: 5/15/2026, 11:11:20 PM
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
       freq=Counter(num%value for num in nums)
       for i in range(len(nums)+1):
        if freq[i%value]==0:
            return i
        freq[i%value]-=1 