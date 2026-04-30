class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r=len(heights)
        c=len(heights[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        pacific=deque()
        atlantic=deque()
        pacificSeen=set()
        atlanticSeen=set()
        for i in range(r):
            for j in range(c):
                if i==0 or j==0:
                    pacific.append((i,j))
                    pacificSeen.add((i,j))
                if i==(r-1) or j==(c-1):
                    atlantic.append((i,j))
                    atlanticSeen.add((i,j))
        while pacific:
            for i in range(len(pacific)):
                row,col=pacific.popleft()
                for dx,dy in directions:
                    newRow=row+dx
                    newCol=col+dy
                    if valid(newRow,newCol) and (newRow,newCol) not in pacificSeen and heights[row][col]<=heights[newRow][newCol]:
                        pacificSeen.add((newRow,newCol))
                        pacific.append((newRow,newCol))
        while atlantic:
            for i in range(len(atlantic)):
                row,col=atlantic.popleft()
                for dx,dy in directions:
                    newRow=row+dx
                    newCol=col+dy
                    if valid(newRow,newCol) and (newRow,newCol) not in atlanticSeen and heights[row][col]<=heights[newRow][newCol]:
                        atlanticSeen.add((newRow,newCol))
                        atlantic.append((newRow,newCol))
        final=atlanticSeen.intersection(pacificSeen)
        finalanswer=[]
        for i in final:
            finalanswer.append(list(i))
        return finalanswer