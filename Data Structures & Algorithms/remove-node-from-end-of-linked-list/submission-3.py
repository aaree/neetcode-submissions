# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        dummy=ListNode(0)
        dummy.next=head
        fast=dummy
        for i in range(n):
            fast=fast.next
        slow=dummy
        prev=None
        if fast is None:
            slow=None
        while fast:
            prev=slow
            fast=fast.next
            slow=slow.next
        if prev:
            prev.next=slow.next
        return dummy.next
        