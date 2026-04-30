class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r=len(heights)
        c=len(heights[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c
        pacific=deque()
        atlantic=deque()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        pacific_seen=set()
        atlantic_seen=set()
        for i in range(r):
            for j in range(c):
                if i==0 or j==0:
                    pacific.append((i,j))
                    pacific_seen.add((i,j))
                if i==r-1 or j==c-1:
                    atlantic.append((i,j))
                    atlantic_seen.add((i,j))
        while len(pacific)>0:
            for i in range(len(pacific)):
                row,col=pacific.popleft()
                for dx,dy in directions:
                    new_row=row+dx
                    new_col=col+dy
                    if (new_row,new_col) not in pacific_seen and valid(new_row,new_col) and heights[new_row][new_col]>=heights[row][col]:
                        pacific_seen.add((new_row,new_col))
                        pacific.append((new_row,new_col))
        while len(atlantic)>0:
            for i in range(len(atlantic)):
                row,col=atlantic.popleft()
                for dx,dy in directions:
                    new_row=row+dx
                    new_col=col+dy
                    if (new_row,new_col) not in atlantic_seen and valid(new_row,new_col) and heights[new_row][new_col]>=heights[row][col]:
                        atlantic_seen.add((new_row,new_col))
                        atlantic.append((new_row,new_col))
        ans=[]
        ans_set=pacific_seen & atlantic_seen
        for i,j in ans_set:
            ans.append([i,j])
        return ans