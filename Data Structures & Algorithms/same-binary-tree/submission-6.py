# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pa=deque()
        qa=deque()
        if p and q:
            pass
        elif not p and not q:
            return True
        elif p or q:
            return False
        pa.append(p)
        qa.append(q)
        equiv=True
        while len(pa)>0:
            for i in range(len(pa)):
                pcurr=pa.popleft()
                qcurr=qa.popleft()
                if pcurr and qcurr:
                    if pcurr.val==qcurr.val:
                        pa.append(pcurr.left)
                        pa.append(pcurr.right)
                        qa.append(qcurr.left)
                        qa.append(qcurr.right)
                    else:
                        return False
                elif pcurr or qcurr:
                    return False
                elif not pcurr and not qcurr:
                    pass
        return True
