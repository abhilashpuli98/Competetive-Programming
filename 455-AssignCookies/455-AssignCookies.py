# Last Updated: 6/21/2026, 7:06:18 PM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        count=l=r=0
        while l<len(g) and r<len(s):
            if s[r]>=g[l]:
                count+=1
                l+=1
            r+=1
        return count