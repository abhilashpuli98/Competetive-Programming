# Last Updated: 6/21/2026, 7:06:35 PM
class Solution(object):
    def thirdMax(self, nums):
        
        nums=list(set(nums))
        n=len(nums)
        if not nums:
            return
        elif n is 1:
            return nums[0]
        elif n is 2:
            return max(nums)
        elif n is 3:
            """if len(nums)<3:
                return self.thirdMax(nums)
            else:"""
            nums=list(nums)
            nums.sort(reverse=True)
            return nums[-1]
        nums.sort(reverse=True)
        return nums[2]