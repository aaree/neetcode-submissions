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
        dic={}
        dummy=head
        while dummy:
            dic[dummy]=Node(dummy.val)
            dummy=dummy.next
        dummy2=head
        while dummy2:
            if dummy2.random:
                rand=dic[dummy2.random]
                dic[dummy2].random=rand
            if dummy2.next:
                nex=dic[dummy2.next]
                dic[dummy2].next=nex
            dummy2=dummy2.next
        return dic[head]