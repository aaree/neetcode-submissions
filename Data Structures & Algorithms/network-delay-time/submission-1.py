class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={}
        for i in range(n+1):
            adj[i]=[]
        for a,b,c in times:
            adj[a].append([c,b])
        shortest={}
        minheap=[[0,k]]
        while minheap:
            w1,n1=heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1]=w1
            for w2,n2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap,[w1+w2,n2])
        maxVal=0
        seen=set()
        for key,val in shortest.items():
            seen.add(key)
            maxVal=max(maxVal,val)
        if len(seen)==n:
            return maxVal
        else:
            return -1
