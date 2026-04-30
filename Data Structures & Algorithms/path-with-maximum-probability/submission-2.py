class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        if len(edges)==0:
            return 0
        adj={}
        for i, val in enumerate(edges):
            if val[0] not in adj:
                adj[val[0]]=[]
            if val[1] not in adj:
                adj[val[1]]=[]
            adj[val[0]].append([succProb[i],val[1]])
            adj[val[1]].append([succProb[i],val[0]])
        minheap=[[1,start_node]]
        shortest={}
        while minheap:
            w1,n1=heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1]=w1
            for w2,n2 in adj.get(n1,[]):
                if n2 not in shortest:
                    heapq.heappush(minheap,[-1*abs(w1*w2),n2])
        if end_node in shortest:
            return -shortest[end_node]
        else:
            return 0
