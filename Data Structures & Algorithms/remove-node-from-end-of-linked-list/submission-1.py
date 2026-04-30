# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n==1:
            return None
        dummy=ListNode(0)
        dummy.next=head
        slow=head
        fast=head
        prev=dummy
        for i in range(n):
            fast=fast.next
        while fast:
            prev=prev.next
            slow=slow.next
            fast=fast.next
        print(slow.val)
        prev.next=slow.next
        return dummy.next