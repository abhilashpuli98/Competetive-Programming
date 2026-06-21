# Last Updated: 6/22/2026, 12:43:02 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        """count=dict()
        for i in range(n):
            count[nums[i]]=count.get(nums[i],0)+1
            if count[nums[i]]>n//2:
                return nums[i]"""
        candidate=None
        count=0
        for i in range(len(nums)):
            if count==0:
                candidate=nums[i]
            count += 1 if nums[i]==candidate else -1
        return candidate
