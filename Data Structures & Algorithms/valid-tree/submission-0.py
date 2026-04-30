class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        adj={}
        for i in range(n):
            adj[i]=[]
        for start,end in edges:
            adj[start].append(end)
            adj[end].append(start)
        loop=set()
        seen=set()
        visited=set()
        ans=[]

        def dfs(node,parent):
            if node in loop:
                return False
            if node in seen:
                return True
            loop.add(node)
            if node in adj:
                for c in adj[node]:
                    if c==parent:
                        continue
                    if not dfs(c,node):
                        return False

            loop.remove(node)
            seen.add(node)
            ans.append(node)
            return True
        dfs(0,None)
        return len(ans)==n