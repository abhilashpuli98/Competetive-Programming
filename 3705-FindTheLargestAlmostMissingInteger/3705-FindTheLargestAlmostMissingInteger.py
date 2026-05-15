# Last Updated: 5/15/2026, 11:10:08 PM
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k==len(nums):
            return max(nums)
        result=-1
        counter=Counter(nums)
        if k==1:
            return max((num for num in counter if counter[num]==1),default=-1)
        if counter[nums[0]]==1:
            result=max(nums[0],result)
        if counter[nums[-1]]==1:
            result=max(nums[-1],result)
        return result 
        
        