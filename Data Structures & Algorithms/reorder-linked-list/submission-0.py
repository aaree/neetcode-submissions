# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        while fast:
            prev=slow
            slow=slow.next
            fast=fast.next
        prev.next=None
        dummy=head
        p=None
        while slow:
            next=slow.next
            curr=slow
            slow.next=p
            slow,p=next,slow
        while dummy and p:
            dnext=dummy.next
            pnext=p.next
            dummy.next,p.next=p,dnext
            dummy=dnext
            p=pnext
        