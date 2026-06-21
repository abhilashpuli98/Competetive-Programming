# Last Updated: 6/21/2026, 7:02:14 PM
class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini=float('inf')
        for i,num in enumerate(nums):
            cs=0
            while num>0:
                temp=num%10
                cs+=temp
                num//=10
            mini=min(mini,cs)
        return mini