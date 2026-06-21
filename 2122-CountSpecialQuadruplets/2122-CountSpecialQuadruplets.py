# Last Updated: 6/21/2026, 7:03:53 PM
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res,n=0,len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for x in range(k+1,n):
                        if nums[i] + nums[j] + nums[k] == nums[x]:
                            res+=1
        return res