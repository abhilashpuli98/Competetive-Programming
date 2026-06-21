# Last Updated: 6/22/2026, 12:45:19 AM
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                p=n-1
                while k<p:
                    csum=nums[i]+nums[j]+nums[k]+nums[p]
                    if csum==target:
                        res.append([nums[i],nums[j],nums[k],nums[p]])
                        k+=1
                        p-=1
                        while k<p and nums[k]==nums[k-1]:
                            k+=1
                        while k<p and nums[p]==nums[p+1]:
                            p-=1
                    elif csum>target:
                        p-=1
                    else:
                        k+=1
        return res