# Last Updated: 6/21/2026, 7:06:28 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        count=0
        def helper(node,reqSum):
            if not node:
                return 
            nonlocal count
            if reqSum==node.val:
                count+=1
            helper(node.left,reqSum-node.val)
            helper(node.right,reqSum-node.val)
        helper(root,targetSum)
        return count+self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum)
         