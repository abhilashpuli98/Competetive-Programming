# Last Updated: 6/22/2026, 12:42:27 AM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        mini=float('inf')
        curr=0
        for right in range(len(nums)):
            curr+=nums[right]
            while curr>=target:
                if mini>(right-left+1):
                    mini=min(mini,right-left+1)
                curr-=nums[left]
                left+=1
        return mini if mini!=float('inf') else 0
