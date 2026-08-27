# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        temp=dummy
        current=head
        
        while current:
            if current.next and current.val==current.next.val:
                while current.next and current.val==current.next.val:
                    current=current.next
                temp.next=current.next
                current=temp.next
            else:
                temp=current
                current=current.next
        return dummy.next


        