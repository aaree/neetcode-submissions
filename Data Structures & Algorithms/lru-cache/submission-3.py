class LinkNode:
    def __init__(self,key,value: int):
        self.key=key
        self.val=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.head=None
        self.tail=None
        self.cache={}
        self.curr=None
        self.cap=capacity
        self.size=0


    def get(self, key: int) -> int:
        print('test')
        if key not in self.cache or self.cache[key] is None:
            return -1
        self.curr=self.cache[key]
        return_value=self.curr.val
        val=self.curr.val
        if self.curr==self.tail:
            return self.curr.val
        elif self.curr==self.head:
            h=self.head
            self.head=self.head.next
            self.head.prev=None
            tail=self.tail
            self.tail.next=h
            self.tail=self.tail.next
            self.tail.prev=tail
            return self.curr.val
        else:
            curr=self.curr
            prev=self.curr.prev
            next=self.curr.next
            self.curr.prev.next=next
            self.curr.next.prev=prev
            tail=self.tail
            self.tail.next=curr
            self.tail=self.tail.next
            self.tail.prev=tail
            return return_value
        

    def put(self, key: int, value: int) -> None:
        if self.head is None:
            new=LinkNode(key,value)
            self.head=new
            self.tail=new
            self.curr=new
            self.cache[key]=new
            self.size+=1
        elif key in self.cache:
            self.curr=self.cache[key]
            if self.curr==self.head:
                h=self.head
                self.head=self.head.next
                self.head.prev=None
                tail=self.tail
                self.tail.next=h
                self.tail=self.tail.next
                self.tail.prev=tail
                self.tail.val=value
            elif self.curr==self.tail:
                self.tail.val=value
            else:
                curr=self.curr
                prev=self.curr.prev
                next=self.curr.next
                self.curr.prev.next=next
                self.curr.next.prev=prev
                tail=self.tail
                self.tail.next=curr
                self.tail=self.tail.next
                self.tail.prev=tail
                self.tail.val=value
        else:
            self.size+=1
            if self.size>self.cap:
                self.size-=1
                head=self.head
                self.head=self.head.next
                del self.cache[head.key]
                new=LinkNode(key,value)
                tail=self.tail
                self.tail.next=new
                self.tail=self.tail.next
                self.tail.prev=tail
                self.cache[key]=self.tail
            else:
                new=LinkNode(key,value)
                tail=self.tail
                self.tail.next=new
                self.tail=self.tail.next
                self.tail.prev=tail
                self.cache[key]=self.tail

        
