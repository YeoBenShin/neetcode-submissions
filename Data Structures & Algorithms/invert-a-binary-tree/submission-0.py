# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert(self, node):
        if node == None:
            return None
        if (node.left == None and node.right == None):
            return None
        if (node.left == None):
            node.left = node.right
            node.right = None
            return self.invert(node.left)
        if (node.right == None):
            node.right = node.left
            node.left = None
            return self.invert(node.right)
        else:
            temp = node.left
            node.left = node.right
            node.right = temp
            return self.invert(node.right), self.invert(node.left)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root
