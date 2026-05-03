class Solution {
    boolean[][] seen;
    public boolean valid(int[][] grid,int row, int col){
        int r=grid.length;
        int c=grid[0].length;
        return (0<=row)&&(row<r)&&(0<=col)&&(col<c)&&(grid[row][col]!=-1);
    }
    public void islandsAndTreasure(int[][] grid) {
        int r=grid.length;
        int c=grid[0].length;
        Deque<int[]> queue=new ArrayDeque<>();
        seen=new boolean[r][c];
        int[][] directions=new int[][]{{0,1},{1,0},{-1,0},{0,-1}};
        for (int i=0;i<r;i++){
            for (int j=0;j<c;j++){
                if (grid[i][j]==0){
                    seen[i][j]=true;
                    queue.offer(new int[] {i,j});
                }
            }
        }
        int traverse=1;
        while (!queue.isEmpty()){
            int len=queue.size();
            for(int i=0;i<len;i++){
                int[] curr=queue.poll();
                int row=curr[0];
                int col=curr[1];
                for (int[] dir:directions){
                    int newRow=row+dir[0];
                    int newCol=col+dir[1];
                    if (valid(grid,newRow,newCol)&&(seen[newRow][newCol]==false)){
                        seen[newRow][newCol]=true;
                        grid[newRow][newCol]=traverse;
                        queue.offer(new int[]{newRow,newCol});
                    }
                }
            }
            traverse+=1;
        }
        
    }
}
