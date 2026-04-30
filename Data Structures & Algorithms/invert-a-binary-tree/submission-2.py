# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        inverse=TreeNode(root.val)
        def dfs(root,inverse):
            if root is None:
                return
            if root.left:
                inverse.right=TreeNode(root.left.val)
                dfs(root.left,inverse.right)
            if root.right:
                inverse.left=TreeNode(root.right.val)
                dfs(root.right,inverse.left)
        dfs(root,inverse)
        return inverse

