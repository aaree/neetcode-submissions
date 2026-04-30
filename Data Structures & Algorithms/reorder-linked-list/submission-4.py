# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        prev=None
        dummy=head
        slow=fast=head
        final=ListNode(0)
        finalDum=final
        while fast and fast.next:
            prev_slow=slow
            slow=slow.next
            fast=fast.next.next
        prev_slow.next=None
        while slow:
            next=slow.next
            slow.next=prev
            prev=slow
            slow=next
        while dummy and prev:
            next=dummy.next
            insert=prev
            prev=prev.next
            dummy.next=insert
            if next:
                insert.next=next
            dummy=next
        

