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
        prev.next=None
        rev=None
        while slow:
            temp=slow.next
            slow.next=rev
            rev=slow
            slow=temp
        even=True
        while rev and dummy:
            if even:
                dum.next=dummy
                dummy=dummy.next
                dum=dum.next
                even= not even
            else:
                dum.next=rev
                dum=dum.next
                rev=rev.next
                even = not even
        while rev:
            dum.next=rev
            rev=rev.next
            dum=dum.next
        while dummy:
            dum.next=dummy
            dummy=dummy.next
            dum=dum.next
        
