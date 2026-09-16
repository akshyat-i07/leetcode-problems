# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        temp=head
        length=0
        while temp!=None:
            length+=1
            temp=temp.next
        stack=[]
        current=head
        for i in range(length//2):
            stack.append(current.val)
            current=current.next
        if length%2!=0:
            current=current.next
        for i in range(length//2):
            if current.val!=stack[-1]:
                return False
            stack.pop(-1)
            current=current.next
        return True

        