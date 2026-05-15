# Last Updated: 5/15/2026, 11:15:32 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result=[]
        q=deque()
        if not root:
            return result
        q.append(root)
        while q:
            level=len(q)
            sublevel=[]
            while level:
                node=q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                sublevel.append(node.val)
                level-=1 
            result.append(sum(sublevel)/len(sublevel))
        return result
        