class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        PriorityQueue<List<Integer>> pq=new PriorityQueue<>((a,b)->a.get(0)-b.get(0));
        Map<Integer,List<List<Integer>>> map=new HashMap<>();
        for (int i=1;i<n+1;i++){
            map.put(i,new ArrayList<>());
        }
        for (int[] time: times){
            int u=time[0];
            int v=time[1];
            int t=time[2];
            map.get(u).add(new ArrayList<>(List.of(t,v)));
        }
        Map<Integer, Integer> shortest=new HashMap<>();
        List<Integer> head=new ArrayList(List.of(0,k));
        pq.offer(head);
        while(!pq.isEmpty()){
            List<Integer> curr=pq.poll();
            int t1=curr.get(0);
            int n1=curr.get(1);
            if(shortest.containsKey(n1)){
                continue;
            }
            shortest.put(n1,t1);
            if (map.containsKey(n1)){
                List<List<Integer>> temp=map.get(n1);
                for(List<Integer> t: temp){
                    int t2=t.get(0);
                    int n2=t.get(1);
                    List<Integer> insert=new ArrayList<>(List.of(t1+t2,n2));
                    pq.offer(insert);
                }
            }
        }
        if (shortest.size()<n){
            return -1;
        }
        int total=0;
        for(Map.Entry<Integer, Integer> e: shortest.entrySet()){
            int temp=e.getValue();
            total=Math.max(total,temp);
        }
        return total;
    
    }
}
