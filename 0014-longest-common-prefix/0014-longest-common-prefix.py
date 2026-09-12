class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0]
        result=""
        for i in range(len(first)):
            for j in strs:
                if i==len(j) or j[i]!=first[i]:
                    return result
            result+=first[i]
        return result


        