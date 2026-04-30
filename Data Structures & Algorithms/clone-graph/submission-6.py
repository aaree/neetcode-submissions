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
        cloneMap={}
        clone=Node(node.val)
        dummy=clone
        cloneMap[node]=clone
        queue=deque()
        cqueue=deque()
        queue.append(node)
        cqueue.append(dummy)
        while len(queue)>0:
            curr=queue.popleft()
            clonecurr=cqueue.popleft()
            for n in curr.neighbors:
                if n in cloneMap and cloneMap[n] not in clonecurr.neighbors:
                    clonecurr.neighbors.append(cloneMap[n])
                    queue.append(n)
                    cqueue.append(cloneMap[n])
                elif n not in cloneMap:
                    cloneMap[n]=Node(n.val)
                    clonecurr.neighbors.append(cloneMap[n])
                    queue.append(n)
                    cqueue.append(cloneMap[n])
        return clone
        


