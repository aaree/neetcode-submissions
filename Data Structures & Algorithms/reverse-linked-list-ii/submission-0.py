# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        first=ListNode(0)
        first.next=head
        dummy=first
        prev=None
        for i in range(left):
            prev=dummy
            dummy=dummy.next
        dummy2=first
        prev2=None
        for i in range(right+1):
            prev2=dummy2
            dummy2=dummy2.next
        prev2.next=None
        revStart=dummy
        prev3=None
        prev.next=None
        while dummy:
            temp=dummy.next
            dummy.next=prev3
            prev3=dummy
            dummy=temp
        prev.next=prev3
        revStart.next=dummy2
        return first.next