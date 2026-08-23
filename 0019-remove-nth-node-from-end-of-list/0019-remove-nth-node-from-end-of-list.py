# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1=head
        length=0
        while temp1!=None:
            length+=1
            temp1=temp1.next
        position=length-n
        if position==0:
            return head.next
        current=head
        count=0
        while count<position-1:
            count+=1
            current=current.next
        temp2=current.next
        current.next=temp2.next
        temp2.next=None
        del temp2

        return head

        