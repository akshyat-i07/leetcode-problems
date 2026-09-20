class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i].isnumeric():
                stack.pop()
            else:
                stack.append(s[i])
        ans=""
        for i in range(len(stack)):
            ans+=stack[i]
        return ans
        