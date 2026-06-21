# Last Updated: 6/21/2026, 7:03:38 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp={}
        roots={}
        for parent,child,isLeft in descriptions:
            if parent not in mp:
                mp[parent]=TreeNode(parent)
            if child not in mp:
                mp[child]=TreeNode(child)
            if isLeft:
                mp[parent].left=mp[child]
            else:
                mp[parent].right=mp[child]
            if roots.get(parent,0)!=-1:
                roots[parent]=1
            roots[child]=-1
        root=None
        for node,state in roots.items():
            if state==1:
                root=node
                break
        return mp[node]