# Last Updated: 5/15/2026, 11:11:54 PM
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        topK=sorted(nums)[-k:]
        res=[]
        for i in range(len(nums)):
            if nums[i] in topK:
                res.append(nums[i])
                topK.remove(nums[i])
        return res