class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        all_num=[]
        for i in range(min(nums),max(nums)+1):
            all_num.append(i)
        ans=[]
        for i in range(len(all_num)):
            if all_num[i] not in nums:
                ans.append(all_num[i])
        return ans

       


        





        