class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={}
        heap=[]
        shortest={}
        for i in range(1,n+1):
            adj[i]=[]
        for u,v,t in times:
            adj[u].append((t,v))
        heapq.heappush(heap,[0,k])
        while heap:
            t1,n1=heapq.heappop(heap)
            if n1 in shortest:
                continue
            shortest[n1]=t1
            if n1 in adj:
                for t2,n2 in adj[n1]:
                    heapq.heappush(heap,[t1+t2,n2])
        print(shortest)
        if len(shortest)!=n:
            return -1
        else:
            return max(shortest.values())