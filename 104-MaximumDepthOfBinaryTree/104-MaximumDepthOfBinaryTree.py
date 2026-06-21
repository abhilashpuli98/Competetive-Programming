# Last Updated: 6/22/2026, 12:43:58 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([root])
        count=0
        while q:
            level=len(q)
            sub_level=[]
            while level:
                node=q.popleft()
                sub_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level-=1
            count+=1
        return count