# Last Updated: 6/22/2026, 12:43:40 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=[]
        path=[]
        def dfs(node):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append(int("".join(path)))
                path.pop()
                return
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            path.pop()
        dfs(root)
        return sum(res)