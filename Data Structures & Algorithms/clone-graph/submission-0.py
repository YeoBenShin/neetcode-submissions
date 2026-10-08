"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        clone = { # real Node -> clone
            node: Node(node.val)
        }

        from collections import deque
        dq = deque([node]) 

        while len(dq) != 0:
            mainNode = dq.popleft()
            cNode = clone[mainNode]

            for neighbour in mainNode.neighbors:
                if neighbour not in clone: # haven't managed before
                    clone[neighbour] = Node(neighbour.val)
                    dq.append(neighbour)
                cNode.neighbors.append(clone[neighbour])
            
        return clone[node]

