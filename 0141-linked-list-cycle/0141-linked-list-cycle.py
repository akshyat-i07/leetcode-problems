# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current=head
        nodes=set()
        while current!=None:
            if current in nodes:
                return True
            else:
                nodes.add(current)
                current=current.next
        return False
        