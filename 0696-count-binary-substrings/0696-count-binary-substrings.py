class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev=0
        current=1
        total=0

        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                current+=1
            else:
                total+=min(prev,current)
                prev=current
                current=1
        total+=min(prev,current)
        return total


        return total
                


        