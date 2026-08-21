# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        nodes=[]
        while current!=None:
            if current in nodes:
                return current
            else:
                nodes.append(current)
                current=current.next
        return None
        
        
        