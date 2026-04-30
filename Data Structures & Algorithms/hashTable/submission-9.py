class HashTable:
    
    def __init__(self, capacity: int):
        self.arr=[None]*capacity
        self.cap=capacity


    def insert(self, key: int, value: int) -> None:
        cnt=0
        ins=key%len(self.arr)
        if self.arr[ins] is None:
            self.arr[ins]=(key,value)
        else:
            while self.arr[ins] is not None:
                if self.arr[ins][0]==key:
                    self.arr[ins]=(key,value)
                    break
                if self.arr[ins][0]=='deleted':
                    self.arr[ins]=(key,value)
                    break
                ins=(ins+1)%len(self.arr)
            self.arr[ins]=(key,value)
        for i in self.arr:
            if i is not None:
                cnt+=1
        if cnt>=self.cap*0.5:
            self.resize()
                    
    def get(self, key: int) -> int:
        print(self.arr)
        ins=key%len(self.arr)
        if self.arr[ins] is None:
            return -1
        while self.arr[ins] is not None:
            if self.arr[ins][0]==key:
                break
            ins=(ins+1)%len(self.arr)
        if self.arr[ins] is None:
            return -1
        else:
            return self.arr[ins][1]

    def remove(self, key: int) -> bool:
        ins=key%len(self.arr)
        if self.arr[ins] is None:
            return False
        while self.arr[ins] is not None and self.arr[ins][0]!=key:
            ins=(ins+1)%len(self.arr)
        if self.arr[ins] is None:
            return False
        else:
            self.arr[ins]='deleted'
            return True


    def getSize(self) -> int:
        cnt=0
        for i in self.arr:
            if i is not None and i!='deleted':
                cnt+=1
        return cnt

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        new_capacity=self.cap * 2
        new_table=[None] * new_capacity
        old=self.arr
        self.arr=new_table
        self.cap=new_capacity
        for val in old:
            if val is not None and val !='deleted':
                self.insert(val[0],val[1])


