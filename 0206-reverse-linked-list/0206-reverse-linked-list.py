# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head

        current=head
        prev= None
        nex=head.next

        while current!=None:
            current.next=prev
            prev=current
            current=nex
            if nex==None:
                continue
            else:
                nex=current.next
        head=prev
        return head


    

        