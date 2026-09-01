class Solution:
    def reverseBits(self, n: int) -> int:
        num=""
        for i in range(32):
            if n%2==1:
                num+="1"
            else:
                num+="0"
            n=n//2
        ans=0
        num=num[::-1]
        for i in range (32):
            ans+=int(num[i])*(2**i)
        return ans


