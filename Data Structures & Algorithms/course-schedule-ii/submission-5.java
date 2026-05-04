class Solution {
    boolean[] seen;
    boolean[] loop;
    List<Integer> answer;
    public boolean dfs(int[][] prerequisites,Map<Integer, List<Integer>> map,int course,List<Integer> answer){
        if (loop[course]!=false){
            return false;
        }
        if (seen[course]!=false){
            return true;
        }
        loop[course]=true;
        if (map.containsKey(course)){
            List<Integer> temp=map.get(course);
            for(int c:temp){
                if (dfs(prerequisites,map,c,answer)==false){
                    return false;
                }
            }
        }
        loop[course]=false;
        seen[course]=true;
        answer.add(course);
        return true;

    }
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<Integer> answer=new ArrayList<>();
        Map<Integer, List<Integer>> map=new HashMap<>();
        seen=new boolean[numCourses];
        loop=new boolean[numCourses];
        for(int i=0;i<numCourses;i++){
            ArrayList temp=new ArrayList<>();
            map.put(i,temp);
        }
        for (int[] course:prerequisites){
            int a=course[0];
            int b=course[1];
            map.get(a).add(b);
        }
        for(int i=0;i<numCourses;i++){
            if (dfs(prerequisites,map,i,answer)==false){
                return new int[]{};
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();

        
    }
}
