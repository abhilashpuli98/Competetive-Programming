# Last Updated: 6/21/2026, 7:03:54 PM
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini,maxi=min(nums),max(nums)
        while maxi>0:
            mini,maxi=maxi,mini%maxi
        return mini