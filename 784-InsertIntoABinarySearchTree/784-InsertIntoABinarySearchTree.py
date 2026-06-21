# Last Updated: 6/21/2026, 7:05:27 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root=TreeNode(val)
            return root
        curr=root
        while curr:
            if curr.val>val:
                if curr.left==None:
                    curr.left=TreeNode(val)
                    return root
                else:
                    curr=curr.left
            else:
                if curr.right==None:
                    curr.right=TreeNode(val)
                    return root
                else:
                    curr=curr.right
        return root
                
            
