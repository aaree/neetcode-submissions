class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> queue=new PriorityQueue<>(Collections.reverseOrder());
        for (int stone:stones){
            queue.offer(stone);
        }
        while (queue.size()>1){
            int one=queue.poll();
            int two=queue.poll();
            int diff=one-two;
            if (diff>0){
                queue.offer(diff);
            }
        }
        if (queue.size()==0){
            return 0;
        }
        else{
            return queue.poll();
        }

    }
}
