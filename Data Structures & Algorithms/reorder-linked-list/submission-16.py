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
        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        dummy=head
        while dummy:
            temp1=dummy.next
            if prev:
                temp2=prev.next
                dummy.next=prev
                prev.next=temp1
                prev=temp2
            dummy=temp1
        
