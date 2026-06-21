# Last Updated: 6/22/2026, 12:44:53 AM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtracker(i):
            if len(nums)==i:
                res.append(nums[:])
                return
            for start in range(i,len(nums)):
                nums[i],nums[start]=nums[start],nums[i]
                backtracker(i+1)
                nums[i],nums[start]=nums[start],nums[i]
        backtracker(0)
        return res