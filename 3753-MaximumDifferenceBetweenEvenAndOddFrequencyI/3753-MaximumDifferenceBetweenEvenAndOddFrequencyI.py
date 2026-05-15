# Last Updated: 5/15/2026, 11:10:00 PM
class Solution:
    def maxDifference(self, s: str) -> int:
        bucket=Counter(s)
        even=float('inf')
        odd=0
        for i in bucket:
            if bucket[i]%2!=0:
                odd=max(bucket[i],odd)
            if bucket[i]%2==0 :
                even=min(even,bucket[i])
        return odd-even
        
        