class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        total=n
        parent={}
        rank={}
        for i in range(n):
            parent[i]=i
            rank[i]=1
        print(parent)
        def find(a):
            while a!=parent[a]:
                parent[a]=parent[parent[a]]
                a=parent[a]
            return parent[a]
        def union(n1,n2):
            a,b=find(n1),find(n2)
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
                total-=1
        return total