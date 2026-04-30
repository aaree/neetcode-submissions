class Node:
    def __init__(self,value,prev=None,next=None):
        self.value=value
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.size=0
        self.cap=capacity
        self.head=Node((0,0))
        self.tail=Node((0,0))
        self.head.next=self.tail
        self.tail.prev=self.head

    def insert(self,node):
        p=self.tail.prev
        p.next=node
        node.prev=p
        node.next=self.tail
        self.tail.prev=node
        self.size+=1
        self.cache[node.value[0]]=node

    def remove(self,node):
        self.size-=1
        node.prev.next=node.next
        node.next.prev=node.prev
        del self.cache[node.value[0]]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value[1]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        if self.size>=self.cap:
            self.remove(self.head.next)
        n=Node((key,value))
        self.insert(n)