# Last Updated: 6/22/2026, 12:44:02 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q=deque([(root,root)])
        while q:
            left,right=q.popleft()
            if not left and not right:
                continue
            if (left and not right) or (not left and right) or left.val!=right.val:
                return False
            q.append((left.left,right.right))
            q.append((left.right,right.left))
        return True
            
        
        