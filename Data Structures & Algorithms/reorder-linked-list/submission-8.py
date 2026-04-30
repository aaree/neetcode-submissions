# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
        prev=None
        first=ListNode(0)
        dum=first
        dummy=head
        slow=fast=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        slow=slow.next
        prev=prev.next
        prev.next=None
        rev=None
        while slow:
            temp=slow.next
            slow.next=rev
            rev=slow
            slow=temp
        while rev and dummy:
            temp=dummy.next
            temp2=rev.next
            dummy.next=rev
            rev.next=temp
            rev=temp2
            dummy=temp

        
