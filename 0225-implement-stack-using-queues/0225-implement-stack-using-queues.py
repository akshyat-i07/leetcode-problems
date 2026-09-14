class MyStack:

    def __init__(self):
        self.items=[]
        

    def push(self, x: int) -> None:
        self.items.append(x)
        n=len(self.items)
        for _ in range(n-1):
            self.items.append(self.items.pop(0))

        

    def pop(self) -> int:
        if len(self.items)==0:
            return "Stack is Empty"
        x=self.items.pop(0)
        return x
        

    def top(self) -> int:
        if len(self.items)==0:
            return "Stack is Empty"
        return self.items[0]

        

    def empty(self) -> bool:
        return len(self.items)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()