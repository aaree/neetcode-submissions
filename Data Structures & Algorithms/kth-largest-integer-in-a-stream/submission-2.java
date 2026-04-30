class KthLargest {
    PriorityQueue<Integer> queue;
    int k;
    public KthLargest(int k, int[] nums) {
        this.queue=new PriorityQueue<>();
        this.k=k;
        for (int num:nums){
            queue.offer(num);
        }
        while (queue.size()>k){
            queue.poll();
        }
    }
    
    public int add(int val) {
        queue.offer(val);
        while(queue.size()>k){
            queue.poll();
        }
        return queue.peek();
    }
}
