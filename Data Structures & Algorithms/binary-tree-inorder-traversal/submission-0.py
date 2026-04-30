# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        trav=[]
        def bst(r):
            nonlocal trav
            if r is None:
                return
            bst(r.left)
            trav.append(r.val)
            bst(r.right)
        bst(root)
        return trav