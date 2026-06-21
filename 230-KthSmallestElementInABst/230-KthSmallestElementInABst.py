# Last Updated: 6/22/2026, 12:42:08 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        curr=root
        while True:
            while curr:
                stack.append(curr)
                curr=curr.left
            node=stack.pop()
            k-=1
            if not k:
                return node.val
            curr=node.right
        