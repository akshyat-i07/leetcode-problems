class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance=0
        new=""

        for i in range(len(s)):
            if s[i]=="(":
                if balance>0:
                    new+=s[i]
                balance+=1
            elif s[i]==")":
                balance-=1
                if balance>0:
                    new+=s[i]
                
        return new
            
        
        