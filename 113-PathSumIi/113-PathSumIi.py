# Last Updated: 6/22/2026, 12:43:51 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res=[]
        path=[]
        def dfs(node,ts):
            if not node :
                return 
            path.append(node.val)
            ts-=node.val
            if not node.left and not node.right and ts==0:
                res.append(path[:])
                path.pop()
                return
            if node.left:
                dfs(node.left,ts)
            if node.right:
                dfs(node.right,ts)
            path.pop()
        dfs(root,targetSum)
        return res