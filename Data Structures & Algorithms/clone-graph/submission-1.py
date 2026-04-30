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
        root=Node(node.val)
        seen={}
        get_nodes={}
        get_nodes[node.val] = root
        def dfs(r,n,prev):
            nonlocal seen
            if n.val in seen:
                return
            seen[n.val]=set()
            if prev is not None:
                if prev.val in set([i.val for i in n.neighbors]):
                    r.neighbors.append(prev)
                    seen[n.val].add(prev.val)
                
            for i in n.neighbors:
                if i.val not in seen[n.val]:
                    if i.val not in get_nodes:
                        new=Node(i.val)
                        get_nodes[i.val]=new
                        r.neighbors.append(new)
                        dfs(new,i,r)
                    else:
                        r.neighbors.append(get_nodes[i.val])
                        dfs(get_nodes[i.val],i,r)
                    seen[n.val].add(i.val)
                    
        dfs(root,node,None)
        return root