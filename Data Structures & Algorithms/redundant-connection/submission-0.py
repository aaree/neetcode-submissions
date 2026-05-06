class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(len(edges)+1)]
        rank=[1]*len(parent)

        def find(num):
            while num!=parent[num]:
                parent[num]=parent[parent[num]]
                num=parent[num]
            return num
        def union(num1,num2):
            a,b=find(num1),find(num2)
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
            if not union(a,b):
                return [a,b]
