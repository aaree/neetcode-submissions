# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def backtrack(root,s):
            nonlocal targetSum
            if root is None:
                return False
            s.append(root.val)
            if not root.left and not root.right and sum(s)==targetSum:
                return True
            if backtrack(root.left,s):
                return True
            if backtrack(root.right,s):
                return True
            s.pop()
            return False
        ans=[]
        boo= backtrack(root,ans)
        return boo
        
