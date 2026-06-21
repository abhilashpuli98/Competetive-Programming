# Last Updated: 6/21/2026, 7:06:33 PM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tsum=sum(nums)
        if tsum%2==1:
            return False
        target=tsum//2
        dp=[False]*(target+1)
        dp[0]=True
        for num in nums:
            for i in range(len(dp)-1,num-1,-1):
                if dp[i]:
                    continue
                if dp[i-num]:
                    dp[i]=dp[i-num]
                if dp[-1]:
                    return True
        return False