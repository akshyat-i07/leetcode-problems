class Solution:
    def beautySum(self, s: str) -> int:

        def calculate(a):
            freq={}
            for ch in a:
                freq[ch]=freq.get(ch,0)+1
            return (max(freq.values())-min(freq.values()))
        total=0

        for i in range(len(s)):
            for j in range(i,len(s)):
                total+=calculate(s[i:j+1])
        return total


        