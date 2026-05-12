# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=slow
        slow=slow.next
        prev.next=None
        p2=None
        while slow:
            temp=slow.next
            slow.next=p2
            p2=slow
            slow=temp
        dummy=head
        while dummy:
            t1=dummy.next
            if p2:            
                t2=p2.next
                dummy.next=p2
                p2.next=t1
                p2=t2
            dummy=t1

            