class TimeMap:

    def __init__(self):
        self.dic={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key]=[]
        self.dic[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        arr=self.dic[key]
        l=0
        r=len(arr)-1
        while r>l:
            m=(r+l+1)//2
            mid=arr[m]
            if mid[1]>timestamp:
                r=m-1
            else:
                l=m
        if arr[l][1]>timestamp:
            return ""
        else:
            return arr[l][0]
