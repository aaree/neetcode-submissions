"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        seen={}
        copy=Node(head.val)
        dummy=copy
        seen[head]=copy
        while head:
            if head.next:
                if head.next not in seen:
                    nextNode=Node(head.next.val)
                    seen[head.next]=nextNode
                    dummy.next=nextNode
                else:
                    dummy.next=seen[head.next]                    
            elif head.next is None:
                dummy.next=None
            if head.random:
                if head.random not in seen:                
                    randomNode=Node(head.random.val)  
                    seen[head.random]=randomNode
                    dummy.random=randomNode
                else:
                    dummy.random=seen[head.random]
            else:
                dummy.random=None
            dummy=dummy.next
            head=head.next
        return copy
            

