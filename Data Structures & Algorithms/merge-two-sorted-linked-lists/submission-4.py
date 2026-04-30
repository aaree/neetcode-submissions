# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0)
        dummy=head
        while list1 and list2:
            list1Val=list1.val if list1 else None
            list2Val=list2.val if list2 else None
            if list1Val<=list2Val:
                dummy.next=ListNode(list1Val)
                dummy=dummy.next
                list1=list1.next
            else:
                dummy.next=ListNode(list2Val)
                dummy=dummy.next
                list2=list2.next
        while list1:
            dummy.next=ListNode(list1.val)
            dummy=dummy.next
            list1=list1.next
        while list2:
            dummy.next=ListNode(list2.val)
            dummy=dummy.next
            list2=list2.next
        return head.next
