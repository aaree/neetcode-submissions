class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map=new HashMap<>();
        int[] answer=new int[k];
        PriorityQueue<List<Integer>> pq=new PriorityQueue<>((a,b)->b.get(0)-a.get(0));
        for (int num: nums){
            map.merge(num,1,Integer::sum);
        }
        
        for (Map.Entry<Integer, Integer> e: map.entrySet()){
            List<Integer> temp=new ArrayList(List.of(e.getValue(),e.getKey()));
            pq.offer(temp);
        }
        for (int i=0;i<k;i++){
            List<Integer> temp2=pq.poll();
            answer[i]=temp2.get(1);
        }
        return answer;



    }
}
