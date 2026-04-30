class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        adj={}
        for i in range(r):
            for j in range(c):
                val=grid[i][j]
                if (i,j) not in adj:
                    adj[(i,j)]=[]
                for dx,dy in directions:
                    newRow=i+dx
                    newCol=j+dy
                    if valid(newRow,newCol):
                        adj[(i,j)].append([grid[newRow][newCol],(newRow,newCol)])
        shortest={}
        minheap=[[grid[0][0],(0,0)]]
        while minheap:
            w1,n1=heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1]=w1
            for w2,n2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap,[max(w1,w2),n2])
        return shortest[(r-1,c-1)]