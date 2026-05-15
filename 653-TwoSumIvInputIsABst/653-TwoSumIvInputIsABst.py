# Last Updated: 5/15/2026, 11:15:29 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited=set()
        def helper(node):
            if not node:
                return False
            if (k-node.val) in visited:
                return True
            visited.add(node.val)
            return helper(node.right) or helper(node.left)
        return helper(root)
        