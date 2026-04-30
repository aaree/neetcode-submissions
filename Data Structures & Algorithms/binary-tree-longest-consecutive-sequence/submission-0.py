# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        maxcnt=0
        def dfs(root,cnt):
            nonlocal maxcnt
            maxcnt=max(cnt,maxcnt)
            if not root:
                return
            if root.left:
                if root.left.val==root.val+1:
                    dfs(root.left,cnt+1)
                else:
                    dfs(root.left,1)
            if root.right:
                if root.right.val==root.val+1:
                    dfs(root.right,cnt+1)
                else:
                    dfs(root.right,1)
        dfs(root,1)
        return maxcnt
