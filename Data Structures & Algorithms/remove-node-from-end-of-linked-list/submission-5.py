# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return None
        fast=head
        for i in range(n):
            fast=fast.next
        slow=head
        if fast is None:
            return head.next
        prev=None
        while fast:
            prev=slow
            fast=fast.next
            slow=slow.next
        prev.next=prev.next.next
        return head