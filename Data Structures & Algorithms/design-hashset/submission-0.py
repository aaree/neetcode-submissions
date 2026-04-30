class MyHashSet:

    def __init__(self):
        self.hashset=[None]*10000

    def add(self, key: int) -> None:
        if key%10000 is None:
            self.hashset[key%10000]=key
        else:
            insert=key%10000
            while self.hashset[insert] is not None:
                insert+=1
            self.hashset[insert]=key

    def remove(self, key: int) -> None:
        remove=key%10000
        if self.hashset[remove]==key:
            self.hashset[remove]=None
        else:
            while self.hashset[remove] is not None:
                if self.hashset[remove]==key:
                    self.hashset[remove]=None
                remove+=1

    def contains(self, key: int) -> bool:
        contain=key%10000
        while self.hashset[contain] is not None:
            if self.hashset[contain]==key:
                return True
            contain+=1
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)