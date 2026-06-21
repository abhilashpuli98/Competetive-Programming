# Last Updated: 6/22/2026, 12:42:49 AM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        #nums[::]=nums[n-k:]+nums[:n-k] 
        #O(k)+O(n-k)+O(n)+o(n)
        def rev(s,e):
            while s<=e:
                nums[s],nums[e]=nums[e],nums[s]
                s+=1
                e-=1
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)