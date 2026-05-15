# Last Updated: 5/15/2026, 11:10:27 PM
import math
from typing import List

class Solution:
    def canFinish(self,T:int,mountainHeight:int,workerTimes:List[int])->bool:
        total=0
        for w in workerTimes:
            x=int((math.sqrt(1+8*T/w)-1)//2)
            while w*x*(x+1)//2>T:
                x-=1
            while w*(x+1)*(x+2)//2<=T:
                x+=1
            total+=x
            if total>=mountainHeight:
                return True
        return total>=mountainHeight

    def minNumberOfSeconds(self,mountainHeight:int,workerTimes:List[int])->int:
        l=0
        r=min(workerTimes)*mountainHeight*(mountainHeight+1)//2
        ans=r
        while l<=r:
            m=(l+r)//2
            if self.canFinish(m,mountainHeight,workerTimes):
                ans=m
                r=m-1
            else:
                l=m+1
        return ans