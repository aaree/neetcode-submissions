class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        self.minVal=math.inf

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minVal=min(val,self.minVal)
        self.minstack.append(self.minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        if len(self.stack)>0:
            self.minVal=self.minstack[-1]
        else:
            self.minVal=math.inf
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
