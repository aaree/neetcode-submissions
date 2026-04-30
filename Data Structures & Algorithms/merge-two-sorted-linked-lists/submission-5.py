# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        head=ListNode(0)
        dummy=head
        while list1 and list2:
            list1val=list1.val
            list2val=list2.val
            if list1val<=list2val:
                dummy.next=list1
                dummy=dummy.next
                list1=list1.next
            else:
                dummy.next=list2
                dummy=dummy.next
                list2=list2.next
        while list1:
            dummy.next=list1
            dummy=dummy.next
            list1=list1.next
        while list2:
            dummy.next=list2
            dummy=dummy.next
            list2=list2.next
        return head.next
