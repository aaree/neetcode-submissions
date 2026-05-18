class Node:

    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cap=capacity
        self.size=0
        self.cache={}

    def delete(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        del self.cache[node.key]
        self.size-=1
    
    def insert(self,node):
        prev=self.tail.prev
        prev.next=node
        node.prev=prev
        node.next=self.tail
        self.tail.prev=node
        self.cache[node.key]=node
        self.size+=1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.delete(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        if self.size>=self.cap:
            self.delete(self.head.next)
        node=Node(key, value)
        self.insert(node)
        