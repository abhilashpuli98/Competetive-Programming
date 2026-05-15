# Last Updated: 5/15/2026, 11:11:43 PM
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        posTracker=0
        negTracker=0
        for i in range(len(nums)):
            if nums[i]>0:
                ans[2*posTracker]=nums[i]
                posTracker+=1
            else:
                ans[2*negTracker+1]=nums[i]
                negTracker+=1
        return ans
