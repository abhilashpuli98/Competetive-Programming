# Last Updated: 6/21/2026, 7:06:38 PM
class Solution:
    def splitter(self,nums,k,co):
        part=1
        splitsum=0
        for i in range(len(nums)):
            if nums[i]>co:
                return False
            if nums[i]+splitsum>co:
                splitsum=nums[i]
                part+=1
            else:
                splitsum+=nums[i]
        if part>k:
            return False
        return True

    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            if self.splitter(nums,k,mid):
                high=mid-1
            else:
                low=mid+1
        return low