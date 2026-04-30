# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        heapq.heapify(heap)
        for node in lists:
            while node:
                heapq.heappush(heap,node.val)
                node=node=node.next
        head=ListNode(0)
        curr=head
        while len(heap)>0:
            val=heapq.heappop(heap)
            curr.next=ListNode(val)
            curr=curr.next
        return head.next