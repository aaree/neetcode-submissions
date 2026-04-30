class Solution {
    boolean[][] seen;
    int maxArea=0;
    int size=0;
    public boolean valid(int[][] grid, int row, int col){
        int r=grid.length;
        int c=grid[0].length;
        return (0<=row)&&(row<r)&&(0<=col)&&(col<c)&&(grid[row][col]==1);
    }
    public void dfs(int[][] grid,int row, int col){
        int[][] direction={{0,1},{1,0},{-1,0},{0,-1}};
        for (int[] dir : direction){
            int newRow=row+dir[0];
            int newCol=col+dir[1];
            if ((valid(grid,newRow,newCol))&&(seen[newRow][newCol]==false)){
                seen[newRow][newCol]=true;
                size++;
                dfs(grid,newRow,newCol);
            }
        }

    }
    public int maxAreaOfIsland(int[][] grid) {
        int r=grid.length;
        int c=grid[0].length;
        if ((r==1) && (c==1)){
            if (grid[0][0]==1){
                return 1;
            }
        }
        seen=new boolean[r][c];
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if ((valid(grid,i,j))&&(seen[i][j]==false)){
                    seen[i][j]=true;
                    size=1;
                    dfs(grid,i,j);
                    maxArea=Math.max(maxArea,size);
                }
            }
        }
        return maxArea;
    }
}
