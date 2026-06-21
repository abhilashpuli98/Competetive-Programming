# Last Updated: 6/21/2026, 7:04:18 PM
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res=0
        MOD=10**9+7
        n=len(nums)
        nums.sort()
        right=n-1
        power=[1]*n
        for i in range(1,n):
            power[i]=(power[i-1]*2)%MOD
        for i,leftValue in enumerate(nums):
            while i<=right and leftValue+nums[right]>target:
                right-=1
            if i<=right:
                res+=power[right-i]
        return res%MOD