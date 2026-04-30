class RandomizedSet:

    def __init__(self):
        self.set={}
        self.arr=[]
        

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.arr.append(val)
        self.set[val]=len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set or len(self.arr)==0:
            return False
        if len(self.arr)==1:
            del self.set[val]
            self.arr.pop()
        elif len(self.arr)>1:
            last=len(self.arr)-1
            loc=self.set[val]
            new=self.arr[last]
            self.arr[loc],self.arr[last]=self.arr[last],self.arr[loc]
            self.arr.pop()
            del self.set[val]
            if val!=new:
                self.set[new]=loc
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0,len(self.arr)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()