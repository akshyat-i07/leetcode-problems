class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        total=2**n
        result=[]

        for num in range(total):
            subset=[]
            for i in range(n):
                if num&(1<<i)!=0:
                    subset.append(nums[i])
            result.append(subset)
        return result
        