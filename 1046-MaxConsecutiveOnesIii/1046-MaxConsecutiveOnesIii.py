# Last Updated: 5/15/2026, 11:14:19 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_zeros = 0
        max_len = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                count_zeros += 1

            while count_zeros > k:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1
                
            max_len = max(max_len, right-left+1)
            
        return max_len