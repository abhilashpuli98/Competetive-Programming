# Last Updated: 6/22/2026, 12:43:56 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        mid = len(nums)//2
        rootNode = TreeNode(nums[mid])
        rootNode.left = self.sortedArrayToBST(nums[:mid])
        rootNode.right = self.sortedArrayToBST(nums[mid+1:])
        return rootNode
