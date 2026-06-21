# Last Updated: 6/21/2026, 7:03:16 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap=[]
        dq=deque([root])
        while dq:
            level=len(dq)
            currSum=0
            for i in range(level):
                curr=dq.popleft()
                currSum+=curr.val
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            heapq.heappush(heap,currSum)
            if len(heap)>k:
                heapq.heappop(heap)
        if k>len(heap):
            return -1
        return heap[0]
