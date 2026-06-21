# Last Updated: 6/21/2026, 7:01:58 PM
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def canFinish(ls,ld,ws,wd):
            mini=float('inf')
            ans=float('inf')
            for i in range(len(ls)):
                mini=min(mini,ls[i]+ld[i])
            for i in range(len(ws)):
                finish=max(mini,ws[i])+wd[i]
                ans=min(ans,finish)
            return ans
        return min(
            canFinish(
                landStartTime,landDuration,waterStartTime,waterDuration
            ),
            canFinish(
                waterStartTime,waterDuration,landStartTime,landDuration
            )
        )