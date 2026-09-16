class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]
        for i in range(len(s)):
            if s[i]=="#":
                if len(s1)!=0:
                    s1.pop()
            else:
                s1.append(s[i])
        
        for i in range(len(t)):
            if t[i]=="#":
                if len(s2)!=0:
                    s2.pop()
            else:
                s2.append(t[i])

        return s1==s2

        