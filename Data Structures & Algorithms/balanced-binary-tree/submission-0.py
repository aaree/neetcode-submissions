# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        result=True
        def dfs(r):
            if r is None:
                return 0
            nonlocal result
            left=dfs(r.left)
            right=dfs(r.right)
            max_val=max(left,right)
            min_val=min(left,right)
            if max_val-min_val>1:
                result=False
            return 1+max(left,right)
        dfs(root)
        return result
