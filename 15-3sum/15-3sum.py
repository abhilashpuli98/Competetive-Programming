# Last Updated: 6/22/2026, 12:45:24 AM
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                csum=nums[i]+nums[j]+nums[k]
                if csum<0:
                    j+=1
                elif csum>0:
                    k-=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return res