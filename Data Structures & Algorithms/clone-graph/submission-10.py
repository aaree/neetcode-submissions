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
        dic={}
        clone=Node(node.val)
        dic[node]=clone
        queue=deque()
        queue.append(node)
        while queue:
            for i in range(len(queue)):
                curr=queue.popleft()
                for c in curr.neighbors:
                    if c not in dic:
                        c2=Node(c.val)
                        dic[c]=c2
                        dic[curr].neighbors.append(c2)
                        queue.append(c)
                    else:
                        dic[curr].neighbors.append(dic[c])
        return dic[node]