# Last Updated: 6/22/2026, 12:43:12 AM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefixp=1
        suffixp=1
        maxi=float('-inf')
        for i in range(len(nums)):
            if prefixp==0:
                prefixp=1
            if suffixp==0:
                suffixp=1
            prefixp*=nums[i]
            suffixp*=nums[len(nums)-i-1]
            maxi=max(maxi,suffixp,prefixp)
        return maxi