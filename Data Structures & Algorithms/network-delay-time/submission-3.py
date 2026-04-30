class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={}
        for i in range(1,n+1):
            adj[i]=[]
        for u,v,t in times:
            adj[u].append((t,v))
        minheap=[[0,k]]
        shortest={}
        while minheap:
            for i in range(len(minheap)):
                w1,n1=heapq.heappop(minheap)
                if n1 in shortest:
                    continue
                shortest[n1]=w1
                for w2,n2 in adj[n1]:
                    heapq.heappush(minheap,[w1+w2,n2])
        maxVal=0
        for i in range(1,n+1):
            if i not in shortest:
                return -1
            maxVal=max(maxVal,shortest[i])
        return maxVal
