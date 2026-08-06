class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        new = list(s)
        l=0
        r=len(new)-1

        while l<r:
            if new[l].isalpha()==True and new[r].isalpha()==True:
                new[l],new[r]=new[r],new[l]
                l+=1
                r-=1
            if new[l].isalpha()==True and new[r].isalpha()==False:
                r-=1
            if new[l].isalpha()==False and new[r].isalpha()==True:
                l+=1
            if new[l].isalpha()==False and new[r].isalpha()==False:
                r-=1
                l+=1
        
        ans=""
        for i in range(len(new)):
            ans+=new[i]
        return ans
        
        