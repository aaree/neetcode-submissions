class Solution {
    boolean[] seen;
    boolean[] loop;
    List<Integer> ans;
    public boolean dfs (int[][] prerequisites,int course,boolean[] loop,boolean[] seen,Map<Integer, List<Integer>> map,List<Integer> ans){
        if (loop[course]==true){
            return false;
        }
        if (seen[course]==true){
            return true;
        }
        loop[course] =true;
        if (map.containsKey(course)){
            for (int c: map.get(course)){
                if (!dfs(prerequisites,c,loop,seen,map,ans)){
                    return false;
                }
            }
        }
        loop[course]=false;
        seen[course]=true;
        ans.add(course);
        return true;            
    }
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        seen=new boolean[numCourses];
        loop=new boolean[numCourses];
        ans=new ArrayList<>();
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
            if (!dfs(prerequisites,c,loop,seen,map,ans)){
                return new int[]{};
            }
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}
