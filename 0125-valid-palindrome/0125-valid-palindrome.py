class Solution:
    def isPalindrome(self, s: str) -> bool:
       result=""
       s=s.lower()
       for i in range(len(s)):
        if s[i].isalnum()!=False:
            result+=s[i]

       l=0
       r=len(result)-1

       while(l<r):
        if result[l]!=result[r]:
            return False
        r-=1
        l+=1
       return True

    
        
