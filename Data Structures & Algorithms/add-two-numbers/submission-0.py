# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        s=ListNode(0)
        dummy=s
        while l1 or l2 or carry>0:
            l1val=l1.val if l1 else 0
            l2val=l2.val if l2 else 0
            total=l1val+l2val+carry
            carry=total//10
            total=total%10
            n=ListNode(total)
            dummy.next=n
            dummy=dummy.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return s.next
