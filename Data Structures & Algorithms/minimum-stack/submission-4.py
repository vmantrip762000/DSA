class MinStack:

    def __init__(self):
        # Secret is to create 2 stacks to track and maintain minimum value
        self.stack = []
        self.minStack = []        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()        

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.minStack[-1]
        
