# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_d=1
        def dfs(r,depth):
            nonlocal max_d
            if r is None:
                return
            if r.left is None and r.right is None:
                if depth>max_d:
                    max_d=depth
                return
            dfs(r.left,depth+1)
            right=dfs(r.right,depth+1)
        dfs(root,1)
        return max_d