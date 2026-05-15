# Last Updated: 5/15/2026, 11:12:37 PM
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x : -x[1])
        maxUnits=0
        for btype,units in boxTypes:
            if truckSize==0:
                return maxUnits
            take=min(truckSize,btype)
            maxUnits+=(take*units)
            truckSize-=take
        return maxUnits