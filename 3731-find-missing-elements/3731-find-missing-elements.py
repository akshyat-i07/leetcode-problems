class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        new=[]
        ans=[]

        for i in range(min(nums),max(nums)+1):
            new.append(i)
        for i in range(len(new)):
            if new[i] not in nums:
                ans.append(new[i])
        return ans


        





        