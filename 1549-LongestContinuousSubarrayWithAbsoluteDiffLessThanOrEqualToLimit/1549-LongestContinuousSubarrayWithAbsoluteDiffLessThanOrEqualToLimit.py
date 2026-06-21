# Last Updated: 6/21/2026, 7:04:28 PM
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        maxq=deque()
        minq=deque()
        left=0
        res=float('-inf')
        for right in range(len(nums)):
            while maxq and maxq[-1]<nums[right]:
                maxq.pop()
            while minq and minq[-1]>nums[right]:
                minq.pop()
            maxq.append(nums[right])
            minq.append(nums[right])
            while maxq[0]-minq[0]>limit:
                if nums[left]==maxq[0]:
                    maxq.popleft()
                if nums[left]==minq[0]:
                    minq.popleft()
                left+=1
            res=max(res,right-left+1)
        return res
            