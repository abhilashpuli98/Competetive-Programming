# Last Updated: 6/22/2026, 12:44:45 AM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefixer=[]
        for x in nums:
            if not prefixer:
                prefixer.append(x)
            else:
                prefixer.append(max(x,prefixer[-1]+x))
        return max(prefixer)
        