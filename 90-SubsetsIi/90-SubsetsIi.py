# Last Updated: 6/22/2026, 12:44:10 AM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        nums.sort()
        def dfs(i):
            if i>len(nums)-1:
                if sub not in res:
                    res.append(sub[:])
                return
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            dfs(i+1)
        dfs(0)
        return res
                
