class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new=[]

        for i in range(len(nums)+1):
            new.append(i)
        for i in range(len(new)):
            if new[i] not in nums:
                return new[i]
        
        