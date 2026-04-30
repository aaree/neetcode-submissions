# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLength=0
        if root is None:
            return maxLength
        def dfs(r):
            nonlocal maxLength
            if r is None:
                return 0
            left= dfs(r.left)
            right=dfs(r.right)
            length=left+right
            maxLength=max(maxLength,length)
            return 1+max(dfs(r.left),dfs(r.right))
        dfs(root)
        return maxLength

        