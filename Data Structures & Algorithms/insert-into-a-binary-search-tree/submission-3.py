# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        def ins(ra,v):
            r=ra
            if r.val<v:
                if r.right:
                    return ins(r.right,v)
                else:
                    r.right=TreeNode(val)
                    return ra 
            if r.val>v:
                if r.left:
                    return ins(r.left,v)
                else:
                    r.left=TreeNode(v)
                    return ra
        dummy=root
        ins(dummy,val)
        return root