class Node{
    int key;
    int value;
    Node prev;
    Node next;

    public Node(int key, int value){
        this.key=key;
        this.value=value;
        this.prev=null;
        this.next=null;

    }
}

class LRUCache {
    Node head;
    Node tail;
    int size;
    int cap;
    Map<Integer, Node> cache;

    public LRUCache(int capacity) {
        this.head=new Node(0,0);
        this.tail=new Node(0,0);
        this.head.next=this.tail;
        this.tail.prev=this.head;
        this.cap=capacity;
        this.size=0;
        this.cache=new HashMap<>();
        
    }

    public void delete(Node node){
        size-=1;
        node.prev.next=node.next;
        node.next.prev=node.prev;
        cache.remove(node.key);

    }
    public void insert(Node node){
        size+=1;
        Node prev=tail.prev;
        prev.next=node;
        node.prev=prev;
        node.next=tail;
        tail.prev=node;
        cache.put(node.key, node);

    }
    
    public int get(int key) {
        if (!cache.containsKey(key)){
            return -1;
        }
        Node node=cache.get(key);
        delete(node);
        insert(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)){
            Node temp=cache.get(key);
            delete(temp);
        }
        if (size>=cap){
            delete(head.next);
        }
        Node n=new Node(key, value);
        insert(n);
    }
}
