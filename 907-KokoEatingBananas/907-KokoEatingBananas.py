# Last Updated: 5/15/2026, 11:14:47 PM
class Solution:
    def hrc(self,speed,piles):
        total=0
        for i in range(len(piles)):
            total+=ceil(piles[i]/speed)
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini=float('inf')
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            ans=self.hrc(mid,piles)
            if ans<=h:
                mini=ans
                high=mid-1
            else:
                low=mid+1
        return low
        