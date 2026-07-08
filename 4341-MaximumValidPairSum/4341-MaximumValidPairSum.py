# Last Updated: 7/9/2026, 12:17:19 AM
class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        best=float('-inf')
        ans=float('-inf')
        for j in range(k,len(nums)):
            best=max(best,nums[j-k])
            ans=max(ans,best+nums[j])
        return ans