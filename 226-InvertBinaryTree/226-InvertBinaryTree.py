# Last Updated: 6/22/2026, 12:42:13 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        org=root
        q=deque([root])
        while q:
            root=q.popleft()
            if not root:
                continue
            root.left,root.right=root.right,root.left
            q.append(root.left)
            q.append(root.right)
        return org