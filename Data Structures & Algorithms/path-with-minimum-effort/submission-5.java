class Solution {
    public boolean valid(int[][] grid, int row, int col){
        int r=grid.length;
        int c=grid[0].length;
        return((0<=row)&&(row<r)&&(0<=col)&&(col<c));
    }
    public int minimumEffortPath(int[][] heights) {
        int r=heights.length;
        int c=heights[0].length;
        int[][] directions=new int[][]{{0,1},{1,0},{-1,0},{0,-1}};
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[0]-b[0]);
        int[] head=new int[]{0,0,0};
        pq.offer(head);
        int[][] shortest=new int[r][c];
        for(int i=0;i<r;i++){
            for (int j=0;j<c;j++){
                shortest[i][j]=Integer.MAX_VALUE;
            }
        }
        while (!pq.isEmpty()){
            int[] curr=pq.poll();
            int w1=curr[0];
            int r1=curr[1];
            int c1=curr[2];
            if (shortest[r1][c1]!=Integer.MAX_VALUE){
                continue;
            }
            shortest[r1][c1]=w1;
            for(int[] dir: directions){
                int newRow=r1+dir[0];
                int newCol=c1+dir[1];
                if (valid(heights,newRow,newCol)){
                    int[] temp=new int[]{Math.max(w1,Math.abs(heights[newRow][newCol]-heights[r1][c1])),newRow,newCol};
                    pq.offer(temp);
                }
            }
        }
        return shortest[r-1][c-1];        
    }
}