# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLength=0
        def dfs(root):
            nonlocal maxLength
            if root is None:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            length=left+right
            maxLength=max(length,maxLength)
            return 1+max(dfs(root.left),dfs(root.right))
        dfs(root)
        return maxLength