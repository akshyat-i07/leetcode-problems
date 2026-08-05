class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        low=nums[0]
        high=nums[len(nums)-1]

        new=[]
        ans=[]

        for i in range(low,high+1):
            new.append(i)
        for i in range(len(new)):
            if new[i] not in nums:
                ans.append(new[i])
        return ans


        





        