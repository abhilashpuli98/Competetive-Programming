# Last Updated: 7/9/2026, 12:18:51 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq=deque([root])
        tracker=0
        maxi=float('-inf')
        maxLevel=float('-inf')
        while dq:
            tracker+=1
            level=len(dq)
            currSum=0
            for i in range(level):
                curr=dq.popleft()
                currSum+=curr.val
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            if maxi<currSum:
                maxi=currSum
                maxLevel=tracker
        return maxLevel
