# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_L=0
        def dfs(r):
            nonlocal max_L
            if r is None:
                return 0
            left=dfs(r.left)
            right=dfs(r.right)
            length=left+right
            if length>max_L:
                max_L=left+right
            return 1+max(left,right)
        dfs(root)
        return max_L