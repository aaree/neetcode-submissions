# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if q is None and p is not None:
            return False
        leftqueue=deque()
        rightqueue=deque()
        leftqueue.append(p)
        rightqueue.append(q)
        while len(leftqueue)>0:
            for i in range(len(leftqueue)):
                pcurr=leftqueue.popleft()
                qcurr=rightqueue.popleft()
                if pcurr.val!=qcurr.val:
                    return False
                if pcurr.left and not qcurr.left:
                    return False
                if pcurr.right and not qcurr.right:
                    return False
                if qcurr.right and not pcurr.right:
                    return False
                if qcurr.left and not pcurr.left:
                    return False
                if pcurr.left and qcurr.left:
                    if pcurr.left.val!=qcurr.left.val:
                        return False
                    leftqueue.append(pcurr.left)
                    rightqueue.append(qcurr.left)
                if pcurr.right and qcurr.right:
                    if pcurr.right.val!=qcurr.right.val:
                        return False
                    leftqueue.append(pcurr.right)
                    rightqueue.append(qcurr.right)
        return True