# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        left_h = self.maxDepth(root.left)
        right_h = self.maxDepth(root.right)

        return 1+left_h if left_h > right_h else 1+right_h