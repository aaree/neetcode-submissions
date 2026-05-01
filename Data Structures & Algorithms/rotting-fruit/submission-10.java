class Solution {
    boolean [][] seen;
    public boolean valid(int[][] grid,int row, int col){
        int r=grid.length;
        int c=grid[0].length;
        return (0<=row)&&(row<r)&&(0<=col)&&(col<c)&&(grid[row][col]!=0);

    }
    public int orangesRotting(int[][] grid) {
        int time=0;
        int r=grid.length;
        int c=grid[0].length;
        seen=new boolean[r][c];
        int[][] directions={{0,1},{1,0},{-1,0},{0,-1}};
        Deque<int[]>queue=new ArrayDeque<>();
        for (int i=0;i<r;i++){
            for (int j=0;j<c;j++){
                if (grid[i][j]==2){
                    seen[i][j]=true;
                    queue.offer(new int[]{i,j});
                }
            }
        }
        while (!queue.isEmpty()){
            int length= queue.size();
            boolean rot=false;
            for (int k=0;k<length;k++){
                int[] curr=queue.poll();
                int row=curr[0];
                int col=curr[1];
                for (int[] dir : directions){
                    int newRow=row+dir[0];
                    int newCol=col+dir[1];
                    if (valid(grid,newRow,newCol)&&(seen[newRow][newCol]==false)){
                        rot=true;
                        seen[newRow][newCol]=true;
                        queue.offer(new int[]{newRow,newCol});
                        grid[newRow][newCol]=2;
                    }
                }
            }
            if (rot==true){
                time+=1;
            }
        }
        boolean fresh=false;
        for(int a=0;a<r;a++){
            for (int b=0;b<c;b++){
                if (grid[a][b]==1){
                    fresh=true;
                }
            }
        }
        if (fresh==true){
            return -1;
        }
        return time;

    }
}
