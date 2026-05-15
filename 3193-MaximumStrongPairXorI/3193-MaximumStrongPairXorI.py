# Last Updated: 5/15/2026, 11:10:55 PM
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i]-nums[j])<=min(nums[i],nums[j]):
                    res=max(res,nums[i]^nums[j])
        return res
