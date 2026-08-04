# Last Updated: 8/5/2026, 12:30:47 AM
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=[float('-inf')]*n
        dp[0]=nums[0]
        dq=deque([0])
        for i in range(1,n):
            while dq and dq[0]<i-k:
                dq.popleft()
            dp[i]=dp[dq[0]]+nums[i]
            while dq and dp[dq[-1]]<=dp[i]:
                dq.pop()
            dq.append(i)
        return dp[-1]