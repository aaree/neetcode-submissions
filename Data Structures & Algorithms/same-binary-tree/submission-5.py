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
        if not p and not q:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        pa.append(p)
        qa.append(q)
        equiv=True
        while len(pa)>0:
            if equiv==False:
                break
            for i in range(len(pa)):
                pnode=pa.popleft()
                qnode=qa.popleft()
                if pnode.val!=qnode.val:
                    equiv=False
                    break
                if qnode and not pnode:
                    equiv=False
                    break
                if qnode.left and not pnode.left:
                    equiv=False
                    break
                if qnode.right and not pnode.right:
                    equiv=False
                    break
                if pnode.left:
                    if not qnode.left:
                        equiv=False
                        break
                    else:
                        if pnode.val!=qnode.val:
                            equiv=False
                            break
                        else:
                            pa.append(pnode.left)
                            qa.append(qnode.left)
                if pnode.right:
                    if not qnode.right:
                        equiv=False
                        break
                    else:
                        if pnode.val!=qnode.val:
                            equiv=False
                            break
                        else:
                            pa.append(pnode.right)
                            qa.append(qnode.right)
        return equiv
