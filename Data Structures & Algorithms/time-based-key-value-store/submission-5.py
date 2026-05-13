class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            arr=self.store[key]
        else:
            return ''
        if arr[0][1]>timestamp:
            return ''
        l=0
        r=len(arr)-1
        while r>l:
            m=(r+l+1)//2
            mid=arr[m]
            if mid[1]>timestamp:
                r=m-1
            else:
                l=m
        return self.store[key][l][0]
