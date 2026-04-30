# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        Total=True
        def equal(a,b):
            nonlocal Total
            if not a and not b:
                return
            if not a or not b:
                Total=False
                return
            if a.val!=b.val:
                Total=False
                return
            equal(a.left,b.left)
            equal(a.right,b.right)
        equal(p,q)
        return Total
            