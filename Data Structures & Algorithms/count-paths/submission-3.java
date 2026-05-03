class Solution {
    Map<String, Integer> memo;
    public boolean valid(int[][] grid,int row, int col){
        int r=grid.length;
        int c=grid[0].length;
        return ((0<=row)&&(row<r)&&(0<=col)&&(col<c));
    }
    public int dfs(int[][] grid,int m, int n, int row, int col){
        if ((row==m-1)&&(col==n-1)){
            return 1;
        }
        String key=row+","+col;
        int total=0;
        if (memo.containsKey(key)){
            return memo.get(key);
        }
        int[][] directions=new int[][] {{0,1},{1,0}};
        for(int[] dir:directions){
            int newRow=row+dir[0];
            int newCol=col+dir[1];
            if (valid(grid,newRow,newCol)){
                total+=dfs(grid,m,n,newRow,newCol);
            }
        }
        memo.put(key,total);
        return memo.get(key);
    }
    public int uniquePaths(int m, int n) {
        memo=new HashMap<>();
        int [][] grid= new int[m][n];
        return dfs(grid,m,n,0,0);
    }
}
