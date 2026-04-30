class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        self.minval=None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minval is None:
            self.minval=val
        else:
            self.minval=min(val,self.minval)
        self.minstack.append(self.minval)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        if len(self.minstack)>0:
            self.minval=self.minstack[-1]
        elif len(self.minstack)==0:
            self.minval=None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minval
