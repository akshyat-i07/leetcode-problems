# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head==None or head.next==None:
            return None
        current=head
        count=0
        while current!=None:
            current=current.next
            count+=1
        middle=count//2
        temp=head
        position=0
        while temp and position<middle-1:
            temp=temp.next
            position+=1
        if temp.next:
            temp.next=temp.next.next
        return head
        
        