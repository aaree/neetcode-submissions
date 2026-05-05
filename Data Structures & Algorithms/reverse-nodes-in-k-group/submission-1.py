# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast=head
        slow=head
        findhead=False
        while fast:
            for i in range(k-1):
                if fast:
                    fast=fast.next
            if not fast:
                break
            next=fast.next
            fast.next=None
            prev=None
            origSlow=slow
            while slow:
                temp=slow.next
                slow.next=prev
                prev=slow
                slow=temp
            origSlow.next=next        
            if findhead:
                prevLoop.next=prev
            if not findhead:
                findhead=True
                head=prev
            slow=next
            fast=next
            prevLoop=origSlow            
        return head

