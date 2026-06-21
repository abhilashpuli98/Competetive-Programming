# Last Updated: 6/22/2026, 12:44:07 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # output=[]
        # def inorder(node):
        #     if not node:
        #         return
        #     left=inorder(node.left)
        #     output.append(node.val)
        #     right=inorder(node.right)
        # inorder(root)
        # return output 
        stack=[]
        res=[]
        curr=root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            node=stack.pop()
            res.append(node.val)
            curr=node.right
        return res
