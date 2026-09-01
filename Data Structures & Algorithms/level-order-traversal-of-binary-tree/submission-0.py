# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = []
        if root != None:
            nodeAtLevel = [root]
        else:
            nodeAtLevel = []
        res = []
        idx = 0
        while len(nodeAtLevel) != 0:
            next_lvl = []
            res_lvl = []
            for node in nodeAtLevel:
                res_lvl.append(node.val)
                if node.left != None:
                    next_lvl.append(node.left)
                if node.right != None:
                    next_lvl.append(node.right)
            nodeAtLevel= next_lvl
            res.append(res_lvl)
            idx += 1
        return res
            
            