class KthLargest {
    PriorityQueue<Integer> queue;
    int k;
    public KthLargest(int k, int[] nums) {
        this.queue=new PriorityQueue<>();
        this.k=k;
        for (int num:nums){
            this.queue.offer(num);
        }
        while (this.queue.size()>k){
            this.queue.poll();
        }
    }
    
    public int add(int val) {
        this.queue.offer(val);
        while(this.queue.size()>k){
            this.queue.poll();
        }
        return this.queue.peek();
    }
}
