class Node:
    def __init__(self, val,prev=None,next=None):
        self.val=val
        self.prev=prev
        self.next=next

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.head=Node(0)
        self.tail=Node(0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cache={}
        self.dupe=set()
        for num in nums:
            if num in self.dupe:
                continue
            elif num in self.cache:
                self.remove(self.cache[num])
                self.dupe.add(num)
            elif num not in self.cache:
                self.insert(Node(num))

    def remove(self,node):
        del self.cache[node.val]
        if node.val in self.cache:
            print('test')
        #print(len(self.cache))
        node.prev.next=node.next
        node.next.prev=node.prev

    def insert(self,node):
        self.cache[node.val]=node
        prev=self.tail.prev
        prev.next=node
        node.prev=prev
        node.next=self.tail
        self.tail.prev=node

    def showFirstUnique(self) -> int:
        #print(len(self.cache))
        if len(self.cache)==0:
            return -1
        return self.head.next.val

    def add(self, value: int) -> None:
        if value in self.dupe:
            pass
        elif value in self.cache:
            self.remove(self.cache[value])
            self.dupe.add(value)
        elif value not in self.cache:
            self.insert(Node(value))

        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)