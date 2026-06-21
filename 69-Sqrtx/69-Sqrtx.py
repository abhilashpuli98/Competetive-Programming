# Last Updated: 6/22/2026, 12:44:31 AM
class Solution:
    def mySqrt(self, x: int) -> int:
        low,high=1,x
        ans=0
        while low<=high:
            mid = (low+high)//2
            if mid*mid<=x:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans