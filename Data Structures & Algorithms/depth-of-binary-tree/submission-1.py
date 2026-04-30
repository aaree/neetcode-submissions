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
        max_length=0
        def bfs(root,val):
            nonlocal max_length            
            if root.left is None and root.right is None:
                max_length=max(max_length,val)
                return val
            if root.left:
                bfs(root.left,val+1)
            if root.right:    
                bfs(root.right,val+1)
        bfs(root,1)
        return max_length