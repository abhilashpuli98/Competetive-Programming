# Last Updated: 7/9/2026, 12:18:45 AM
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key=lambda x : (x[0],-x[1]))
        count=0
        max_end=0
        for s,e in intervals:
            if e<=max_end:
                count+=1
            else:
                max_end=e
        return n-count