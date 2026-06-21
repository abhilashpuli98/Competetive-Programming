# Last Updated: 6/22/2026, 12:44:59 AM
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]
        combos=[]
        def backtracker(start,csum):
            if csum>target:
                return
            if csum==target:
                res.append(combos[:])
                return
            for i in range(start,len(nums)):
                combos.append(nums[i])
                backtracker(i,csum+nums[i])
                combos.pop()
        backtracker(0,0)
        return res