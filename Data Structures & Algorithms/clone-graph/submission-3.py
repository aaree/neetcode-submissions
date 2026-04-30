"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        rep={}
        def copy(r,n):
            for i in n.neighbors:
                if i.val in rep:
                    r.neighbors.append(rep[i.val])
                else:
                    new=Node(i.val)
                    rep[i.val]=new                    
                    r.neighbors.append(new)
                    copy(new,i)
        root=Node(node.val)
        copy(root,node)
        return root
                