class Node:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.prev=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def insert(self,node):
        prev=self.tail.prev
        prev.next=node
        node.prev=prev
        node.next=self.tail
        self.tail.prev=node

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

class LRUCache:

    def __init__(self, capacity: int):
        self.ll=LinkedList()
        self.cap=capacity
        self.size=0
        self.cache={}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.ll.remove(node)
        self.ll.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            del self.cache[key]
            self.size-=1
            self.ll.remove(node)
        elif self.size>=self.cap:
            node=self.cache[self.ll.head.next.key]
            del self.cache[self.ll.head.next.key]
            self.size-=1
            self.ll.remove(node)
        n=Node(key,value)
        self.cache[key]=n
        self.size+=1
        self.ll.insert(n)
