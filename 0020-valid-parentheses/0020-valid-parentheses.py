class Solution:
    def isValid(self, s: str) -> bool:
        brackets={")":"(","}":"{","]":"["}
        stack=[]
        for i in range(len(s)):
            if s[i] in brackets.keys():
                if len(stack)==0:
                    return False
                elif brackets[s[i]]!=stack[-1]:
                    return False
                else:
                    stack.pop(-1)
            else:
                stack.append(s[i])
        return len(stack)==0
            
            

        
        
        