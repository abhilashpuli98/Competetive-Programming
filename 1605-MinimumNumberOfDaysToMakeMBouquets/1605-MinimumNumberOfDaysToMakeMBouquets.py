# Last Updated: 5/15/2026, 11:13:08 PM
class Solution:
    def isPossible(self,bloomDay,day,m,k):
        count=0
        nb=0
        for x in bloomDay:
            if x<=day:
                count+=1
            else:
                nb+=(count//k)
                count=0
        nb+=(count//k)
        if nb>=m:
            return True
        return False
    def minmax(self,bloomDay):
        mini,maxi=float('inf'),float('-inf')
        for x in bloomDay:
            if mini>x:
                mini=x
            if maxi<x:
                maxi=x
        return mini,maxi
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low,high=self.minmax(bloomDay)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if self.isPossible(bloomDay,mid,m,k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        