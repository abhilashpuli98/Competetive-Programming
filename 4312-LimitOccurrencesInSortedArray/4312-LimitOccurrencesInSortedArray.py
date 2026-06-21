# Last Updated: 6/21/2026, 7:01:47 PM
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res=[]
        n=len(nums)
        i=0
        while i<n:
            current=nums[i]
            count=0
            while i<n and current==nums[i]:
                count+=1
                i+=1
            if count>=k:
                res.extend([current]*k)
            else:
                res.extend([current]*count)
        return res