# Last Updated: 6/21/2026, 7:02:23 PM
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single=0
        other=0
        for num in nums:
            if 0<=num<=9:
                single +=num
            else:
                other+=num
        return False if not single-other else True
