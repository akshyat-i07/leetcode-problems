class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        rev_y=y[::-1]

        return y==rev_y

        

        