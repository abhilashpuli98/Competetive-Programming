# Last Updated: 5/15/2026, 11:11:38 PM
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        """n=len(nums)
        Newnums=[]
        if len(nums)==1:
            return nums[0]
        while len(nums)>1:
            for i in range(len(nums)-1):
                Newnums.append((nums[i]+nums[i+1])%10)
            nums=Newnums
            Newnums=[]
        return nums[0]"""
        if len(nums)==1:
            return nums[0]
        newNums=[0]*(len(nums)-1)
        for i in range(len(nums)-1):
            newNums[i]=(nums[i]+nums[i+1])%10
        return self.triangularSum(newNums)
