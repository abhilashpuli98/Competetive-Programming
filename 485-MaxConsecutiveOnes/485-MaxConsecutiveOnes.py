# Last Updated: 6/21/2026, 7:06:10 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        maxi=0
        for j in range(len(nums)):
            if nums[j]==0:
                i=j+1
            else:
                maxi=max(maxi,j-i+1)
        
        return maxi