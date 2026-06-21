# Last Updated: 6/21/2026, 7:04:53 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp={}
        q=deque([(root,0,0)])
        while q:
            node,r,c=q.popleft()
            if c not in mp:
                mp[c]=[]
            mp[c].append([r,node.val])
            if node.left:
                q.append([node.left,r+1,c-1])
            if node.right:
                q.append([node.right,r+1,c+1])
        #print(sorted(mp))
        res=[]
        for key in sorted(mp):
            col_list=[]
            for lst in sorted(mp[key],key=lambda x:(x[0],x[1])):
                col_list.append(lst[1])
            res.append(col_list)
        return res

