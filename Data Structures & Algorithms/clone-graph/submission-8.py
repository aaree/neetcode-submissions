"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mapping={}
        queue=deque()
        root=node
        clone=Node(node.val)
        mapping[node]=clone
        queue.append(root)
        while len(queue)>0:
            curr=queue.pop()
            cloneCurr=mapping[curr]
            for nextNode in curr.neighbors:
                if nextNode not in mapping:
                    nextClone=Node(nextNode.val)
                    mapping[nextNode]=nextClone
                    queue.append(nextNode)
                cloneCurr.neighbors.append(mapping[nextNode])
                
        return mapping[node]

