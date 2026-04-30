class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r=len(heights)
        c=len(heights[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        pacific=set()
        atlantic=set()
        def dfs(row,col,seen):
            nonlocal atlantic
            nonlocal pacific
            seen.add((row,col))
            for d in directions:
                dx,dy=d
                new_row=row+dx
                new_col=col+dy
                if valid(new_row,new_col) and (new_row,new_col) not in seen and heights[new_row][new_col]>=heights[row][col]:
                    dfs(new_row,new_col,seen)
        for i in range(r):
            for j in range(c):
                if i==0 or j==0:
                    pacific.add((i,j))
                    dfs(i,j,pacific)
                if i==(r-1) or j==(c-1):
                    atlantic.add((i,j))
                    dfs(i,j,atlantic)
        total=atlantic.intersection(pacific)
        ans=[]
        for i in total:
            ans.append([i[0],i[1]])
        return ans
