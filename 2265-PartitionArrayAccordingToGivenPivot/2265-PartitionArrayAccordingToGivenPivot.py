# Last Updated: 6/21/2026, 7:03:41 PM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [0] * n
        i = 0
        j = len(nums) - 1
        left = 0
        right = len(nums) - 1
        while i < n:
            if nums[i] < pivot:
                res[left] = nums[i]
                left += 1
            if nums[j] > pivot:
                res[right] = nums[j]
                right -= 1
            i += 1
            j -= 1
        while left <= right:
            res[left] = pivot
            left += 1
        return res
