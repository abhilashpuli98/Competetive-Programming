# Last Updated: 5/15/2026, 11:13:06 PM
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[0]*n
        result=0
        for i in range(n):
            nums[i]=start+2*i
            result^=nums[i]
        return result