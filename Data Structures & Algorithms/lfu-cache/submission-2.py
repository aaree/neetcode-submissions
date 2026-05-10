class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
        self.freq=1
class LinkedList:
    def __init__(self):
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def insert(self,node):
        prev=self.tail.prev
        node.prev=prev
        prev.next=node
        self.tail.prev=node
        node.next=self.tail

    def delete(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

class LFUCache:

    def __init__(self, capacity: int):
        self.size=0
        self.cap=capacity
        self.cache={}
        self.freq={}
        self.minVal=math.inf

    def update(self,node):
        freq=node.freq
        newFreq=node.freq+1
        node.freq+=1
        oldLL=self.freq[freq]
        if newFreq not in self.freq:
            ll=LinkedList()
            self.freq[newFreq]=ll
        else:
            ll=self.freq[newFreq]
        oldLL.delete(node)
        if oldLL.head.next==oldLL.tail:
            del self.freq[freq]                
        ll.insert(node)
        if self.minVal==freq:
            if freq not in self.freq:
                self.minVal=newFreq


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.update(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return
        if key not in self.cache:
            if self.size==self.cap:
                n=self.freq[self.minVal].head.next
                del self.cache[n.key]
                self.freq[self.minVal].delete(n)
                if self.freq[self.minVal].head.next==self.freq[self.minVal].tail:
                    del self.freq[self.minVal]
                self.size-=1
            n=Node(key,value)
            self.cache[key]=n
            self.minVal=n.freq
            if n.freq not in self.freq:
                self.freq[n.freq]=LinkedList()
            self.freq[n.freq].insert(n)
            self.size+=1
        else:
            n=self.cache[key]
            self.update(n)
            n.val=value
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)