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
        seen={}
        queue=deque()
        queue.append(node)
        seen[node]=set()
        queue2=deque()
        clone_top=Node(node.val)
        queue2.append(clone_top)
        mapping={}
        mapping[node]=clone_top
        while len(queue)>0:
            for i in range(len(queue)):                
                curr=queue.popleft()
                if curr not in seen:
                    seen[curr]=set()
                clone=queue2.popleft()
                for i in curr.neighbors:
                        if i not in seen[curr]:
                            seen[curr].add(i)
                            if i not in mapping:
                                new_clone=Node(i.val)
                                mapping[i]=new_clone
                                clone.neighbors.append(new_clone)
                                queue.append(i)
                                queue2.append(new_clone)
                            else:
                                new_clone=mapping[i]
                                clone.neighbors.append(new_clone)
        return clone_top
