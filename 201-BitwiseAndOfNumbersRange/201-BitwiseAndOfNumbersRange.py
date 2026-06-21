# Last Updated: 6/22/2026, 12:42:39 AM
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count=0
        while left!=right:
            left=left>>1
            right=right>>1
            count+=1
        return left<<count