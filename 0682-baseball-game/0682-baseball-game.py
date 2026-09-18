class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack=[]
        for i in range(len(operations)):
            if operations[i]=="+":
                if len(stack)<2:
                    stack.append(stack[-1])
                else:
                    total=stack[-1]+stack[-2]
                    stack.append(total)
            elif operations[i]=="C":
                stack.pop()
            elif operations[i]=="D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(operations[i]))
        ans=0
        for i in range(len(stack)):
            ans+=stack[i]
        return ans
        