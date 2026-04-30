# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new=ListNode(0)
        new2=new
        while list1 is not None and list2 is not None:
            if list1.val<=list2.val:
                new2.next=ListNode(list1.val)
                new2=new2.next
                list1=list1.next
            else:
                new2.next=ListNode(list2.val)
                new2=new2.next
                list2=list2.next
        while list1 is not None:
            new2.next=ListNode(list1.val)
            list1=list1.next
            new2=new2.next
        while list2 is not None:
            new2.next=ListNode(list2.val)
            new2=new2.next
            list2=list2.next
        return new.next
            
