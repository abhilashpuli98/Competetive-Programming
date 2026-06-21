# Last Updated: 6/21/2026, 7:05:20 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res=float('inf')
        prev=None
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            nonlocal prev
            nonlocal res
            if prev:
                res=min(res,node.val-prev.val)
            prev=node
            inorder(node.right)
        inorder(root)
        return res