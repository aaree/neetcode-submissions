class MinStack {
    Deque<Integer> dq;
    Deque<Integer> mindq;
    int min=Integer.MAX_VALUE;
    public MinStack() {
        this.dq=new ArrayDeque<>();
        this.mindq=new ArrayDeque<>();
    }
    
    public void push(int val) {
        min=Math.min(min,val);
        mindq.push(min);
        dq.push(val);
    }
    
    public void pop() {
        int val=dq.pop();
        mindq.pop();
        if (mindq.size()>0){
            min=mindq.peek();
        }else{
            min=Integer.MAX_VALUE;
        }
    }
    
    public int top() {
        return dq.peek();
    }
    
    public int getMin() {
        return mindq.peek();
    }
}
