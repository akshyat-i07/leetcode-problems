class Solution:
    def maxDepth(self, s: str) -> int:
        balance=0
        maximum=0

        for ch in s:
            if ch=="(":
                balance+=1
                if balance>maximum:
                    maximum=balance
            if ch==")":
                balance-=1
        return maximum