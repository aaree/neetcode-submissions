class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent={}
        rank={}
        for i in range(n):
            parent[i]=i
            rank[i]=1
        
        def find(n):
            while n!=parent[n]:
                parent[n]=parent[parent[n]]
                n=parent[n]
            return parent[n]
        
        def union(n1,n2):
            a,b = find(n1),find(n2)
            if a==b:
                return False
            if rank[a]>rank[b]:
                parent[b]=a
                rank[a]+=rank[b]
            else:
                parent[a]=b
                rank[b]+=rank[a]
            return True

        for a,b in edges:
            if union(a,b):
                n-=1
        return n