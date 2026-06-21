# Last Updated: 6/21/2026, 7:06:06 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        prev=None
        count=0
        maxCount=0
        ans=[]
        stack=[]
        curr=root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            node=stack.pop()
            if node.val==prev:
                count+=1
            else:
                count=1
            if maxCount<count:
                maxCount=count
                ans=[node.val]
            elif count==maxCount:
                ans.append(node.val)
            prev=node.val
            curr=node.right
        return ans


            