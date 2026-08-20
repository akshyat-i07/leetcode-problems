# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        prev=None
        nex=None

        while current!=None:
            nex=current.next
            current.next=prev
            prev=current
            current=nex
        head=prev
        temp=head
        while temp!=None:
            return temp
            temp=temp.next
        