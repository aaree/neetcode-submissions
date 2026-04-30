class Node{
    int value;
    int key;
    Node prev;
    Node next;

    public Node(int key, int value){
        this.value=value;
        this.key=key;
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
        this.cap=capacity;
        this.head=new Node(0,0);
        this.tail=new Node(0,0);
        this.head.next=this.tail;
        this.tail.prev=this.head;
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
        Node prev=tail.prev;
        prev.next=node;
        node.prev=prev;
        node.next=tail;
        tail.prev=node;
        size+=1;
        cache.put(node.key,node);
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)){
            return -1;
        }
        Node n=cache.get(key);
        delete(n);
        insert(n);
        return n.value;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)){
            delete(cache.get(key));
        }
        if (size>=cap){
            delete(head.next);
        }
        Node newNode=new Node(key,value);
        insert(newNode);
    }
}
