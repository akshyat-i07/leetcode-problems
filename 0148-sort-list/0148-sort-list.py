# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        nums=[]
        temp=head
        while temp!=None:
            nums.append(temp.val)
            temp=temp.next
        nums.sort()
        current=head
        for i in range(len(nums)):
            current.val=nums[i]
            current=current.next
        return head

        
        