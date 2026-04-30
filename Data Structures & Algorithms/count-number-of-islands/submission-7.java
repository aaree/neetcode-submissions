class Solution {
    boolean[][] visited;
    public boolean valid(char grid[][],int row, int col){
        int r=grid.length;
        int c=grid[0].length;
        return (0<=row)&&(row<r)&&(0<=col)&&(col<c)&&(grid[row][col]=='1');

    }
    public void dfs(char[][] grid, int row, int col){
        int[][] directions={{0,1},{0,-1},{1,0},{-1,0}};
        for (int[] dir: directions){
            int newRow=row+dir[0];
            int newCol=col+dir[1];
            if ((valid(grid,newRow,newCol)) && (visited[newRow][newCol]==false)){
                visited[newRow][newCol]=true;
                dfs(grid,newRow,newCol);
            }
        }

    }
    public int numIslands(char[][] grid) {
        int cnt=0;
        int r=grid.length;
        int c=grid[0].length;
        visited=new boolean[r][c];
        for (int i=0;i<r;i++){
            for (int j=0;j<c;j++){
                int[] next={i,j};
                if ((valid(grid,i,j))&&(visited[i][j]==false)){
                    cnt++;
                    visited[i][j]=true;
                    dfs(grid,i,j);
                }
            }
        }
        return cnt;
    }
}
