# Last Updated: 8/5/2026, 12:31:54 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque([(root,0)])
        maxi=1
        while q:
            _,first=q[0]
            _,last=q[-1]
            maxi=max(maxi,last-first+1)
            lvl_len=len(q)
            for i in range(lvl_len):
                node,index=q.popleft()
                if node.left:
                    q.append((node.left,2*index))
                if node.right:
                    q.append((node.right,2*index+1))
        return maxi
