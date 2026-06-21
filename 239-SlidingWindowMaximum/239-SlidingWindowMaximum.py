# Last Updated: 6/22/2026, 12:41:57 AM
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        q=deque()
        res=[]
        for i in range(n):
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            if q and q[0]<=i-k:
                q.popleft()
            q.append(i)
            if i>=k-1:
                res.append(nums[q[0]])
        return res
