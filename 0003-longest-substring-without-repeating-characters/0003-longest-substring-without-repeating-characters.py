class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum=0
        for i in range(len(s)):
            new=""
            for j in range(i,len(s)):
                if s[j] in new:
                    break
                new+=s[j]
                maximum=max(maximum,len(new))
        return maximum
                
        
        