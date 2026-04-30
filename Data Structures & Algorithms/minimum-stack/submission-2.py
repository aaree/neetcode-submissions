class MinStack:

    def __init__(self):
        self.stack=[]
        self.minvalue=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minvalue)>0:
            if self.minvalue[-1]>=val:
                self.minvalue.append(val)
        else:
            self.minvalue.append(val)

    def pop(self) -> None:
        val=self.stack.pop()
        if self.minvalue[-1]==val:
            self.minvalue.pop()
        return val

    def top(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.minvalue)>0:
            return self.minvalue[-1]
        else:
            return None
