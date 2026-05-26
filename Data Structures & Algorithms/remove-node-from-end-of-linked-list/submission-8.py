# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root=ListNode(0)
        root.next=head
        prev=root
        dummy=root
        for i in range(n):
            dummy=dummy.next
        while dummy:
            if dummy.next is None:
                break
            prev=prev.next
            dummy=dummy.next
        if prev and prev.next:
            prev.next=prev.next.next
        else:
            prev.next=None
        return root.next           