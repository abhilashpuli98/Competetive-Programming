# Last Updated: 6/22/2026, 12:41:41 AM
class Solution:
    def lengthOfLIS(self, nums):
        n=len(nums)
        dp=[[-1]* (n+1) for _ in range(n+1)]
        def rec(i,prev):
            if i==len(nums):
                return 0
            if dp[i][prev+1]!=-1:
                return dp[i][prev+1]
            include=0
            if prev==-1 or nums[i]>nums[prev]:
                include=1+rec(i+1,i)
            exc=rec(i+1,prev)
            dp[i][prev+1]=max(include,exc)
            return dp[i][prev+1]
        return rec(0,-1)
        
        