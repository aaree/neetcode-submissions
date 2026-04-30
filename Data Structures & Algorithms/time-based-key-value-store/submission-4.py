class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr=self.store[key]
        l=0
        r=len(arr)-1
        while r>l:
            m=(r+l+1)//2
            mid=arr[m]
            if mid[0]>timestamp:
                r=m-1
            else:
                l=m
        if arr[l][0]>timestamp:
            return ""
        else:
            return arr[l][1]
        
