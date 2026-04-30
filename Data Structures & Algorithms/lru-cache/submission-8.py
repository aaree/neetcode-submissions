class Node:
    def __init__(self,val,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.size=0
        self.head=Node((0,0))
        self.tail=Node((0,0))
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cache={}

    def insert(self,node):
        self.size+=1
        self.cache[node.val[0]]=node
        prev=self.tail.prev
        prev.next=node
        node.prev=prev
        node.next=self.tail
        self.tail.prev=node

    def remove(self,node):
        self.size-=1
        node.prev.next=node.next
        node.next.prev=node.prev
        del self.cache[node.val[0]]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            n=self.cache[key]
            self.remove(n)
            self.insert(n)
            return n.val[1]

    def put(self, key: int, value: int) -> None:
        insertNode=Node((key,value))
        if key in self.cache:
            self.remove(self.cache[key])
        if self.size>=self.cap:
            self.remove(self.head.next)
        self.insert(insertNode)