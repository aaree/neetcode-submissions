class Solution {
    boolean[] seen;
    boolean[] loop;
    int[] ans;
    public boolean dfs (int[][] prerequisites,int course,boolean[] loop,boolean[] seen,int[] ans,Map<Integer, List<Integer>> map){
        if (loop[course]==true){
            return false;
        }
        if (seen[course]==true){
            return true;
        }
        loop[course] =true;
        if (map.containsKey(course)){
            for (int c: map.get(course)){
                if (!dfs(prerequisites,c,loop,seen,ans,map)){
                    return false;
                }
            }
        }
        loop[course]=false;
        seen[course]=true;
        return true;            
    }
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        seen=new boolean[numCourses];
        loop=new boolean[numCourses];
        ans=new int[numCourses];
        Map<Integer, List<Integer>> map=new HashMap<>();
        for (int i=0;i<numCourses;i++){
            map.put(i,new ArrayList<>());
        }
        for (int[] course:prerequisites){
            int a=course[0];
            int b=course[1];
            map.get(a).add(b);
        }
        for (int c=0;c<numCourses;c++){
            if (!dfs(prerequisites,c,loop,seen,ans,map)){
                return false;
            }
        }
        return true;


    }
}
