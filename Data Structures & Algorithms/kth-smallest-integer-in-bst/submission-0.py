# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        all_values=[]
        def bst(r,v):
            if r is None:
                return
            bst(r.left,v)
            all_values.append(r.val)
            bst(r.right,v)
        bst(root,k)
        return all_values[k-1]