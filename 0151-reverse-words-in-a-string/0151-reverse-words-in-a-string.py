class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        ans=""
        for i in range(len(words)-1,-1,-1):
            ans+=words[i]+" "
        return ans.strip()


        