class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum=0
        for i in range(len(s)):
            new=""
            for j in range(i,len(s)):
                if s[j] in new:
                    break
                new=s[i:j+1]
                maximum=max(maximum,len(new))
        return maximum
        
        