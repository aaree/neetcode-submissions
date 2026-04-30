class LinkNode:
    def __init__(self,val,prev=None,next=None):
        self.val=val
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.size=0
        self.tail=LinkNode((0,0))
        self.head=LinkNode((0,0))
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cap=capacity

    def delete(self,node):
        key,val=node.val
        del self.cache[key]
        self.size-=1
        node.prev.next=node.next
        node.next.prev=node.prev

    def insert(self,node):
        prev=self.tail.prev
        prev.next=node
        node.prev=prev
        node.next=self.tail
        self.tail.prev=node
        #print(self.tail.prev.val[1])
        self.size+=1
        key, val = node.val
        self.cache[key]=node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.delete(node)
        self.insert(node)
        #print(self.tail.prev.val[1])
        #print(node.val[1])
        return node.val[1]

    def put(self, key: int, value: int) -> None:
        node=LinkNode((key,value))
        if key in self.cache:
            self.delete(self.cache[key])
        self.insert(node)
        if self.size>self.cap:
            self.delete(self.head.next)        
