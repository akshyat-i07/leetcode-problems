class MinStack:

    def __init__(self):
        self.items=[]
        

    def push(self, value: int) -> None:
        if len(self.items)==0:
            self.items.append([value,value])
        else:
            minimum=min(value,self.items[-1][1])
            self.items.append([value,minimum])
        
    def pop(self) -> None:
        if len(self.items)==0:
            return "Empty Stack"
        x=self.items.pop()
        return x
        

    def top(self) -> int:
        if len(self.items)==0:
            return "Empty Stack"
        return self.items[-1][0]

        

    def getMin(self) -> int:
        if len(self.items)==0:
            return "Empty Stack"
        return self.items[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()