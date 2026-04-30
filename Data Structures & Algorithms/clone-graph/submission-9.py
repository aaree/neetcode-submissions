"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adj={}
        cloneadj={}
        if node is None:
            return None
        adj[node.val]=node
        head=Node(node.val)
        cloneadj[node.val]=head
        queue=deque()
        queue.append(node)
        while queue:
            curr=queue.popleft()
            nex=curr.neighbors
            for n in nex:
                if n.val in cloneadj:
                    nod=cloneadj[n.val]
                else:
                    nod=Node(n.val)
                    cloneadj[n.val]=nod
                    queue.append(n)
                cloneadj[curr.val].neighbors.append(nod)
        return head
