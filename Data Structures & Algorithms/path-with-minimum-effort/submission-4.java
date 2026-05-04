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
        PriorityQueue<List<Integer>> pq = new PriorityQueue<>((a,b)->a.get(0)-b.get(0));
        List<Integer> head=new ArrayList(List.of(0,0,0));
        pq.offer(head);
        int[][] shortest=new int[r][c];
        for(int i=0;i<r;i++){
            for (int j=0;j<c;j++){
                shortest[i][j]=Integer.MAX_VALUE;
            }
        }
        while (!pq.isEmpty()){
            List<Integer> curr=pq.poll();
            int w1=curr.get(0);
            int r1=curr.get(1);
            int c1=curr.get(2);
            if (shortest[r1][c1]!=Integer.MAX_VALUE){
                continue;
            }
            shortest[r1][c1]=w1;
            for(int[] dir: directions){
                int newRow=r1+dir[0];
                int newCol=c1+dir[1];
                if (valid(heights,newRow,newCol)){
                    List<Integer> temp=new ArrayList<>(List.of(Math.max(w1,Math.abs(heights[newRow][newCol]-heights[r1][c1])),newRow,newCol));
                    pq.offer(temp);
                }
            }
        }
        return shortest[r-1][c-1];        
    }
}