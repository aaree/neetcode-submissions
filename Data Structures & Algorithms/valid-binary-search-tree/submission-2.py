# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid=True
        def dfs(node,lower,upper):
            nonlocal isValid
            if node is None:
                return
            if node.val<=lower or node.val>=upper:
                isValid=False
                return
            if node.left:
                dfs(node.left,lower,node.val)
            if node.right:
                dfs(node.right,node.val,upper)
        dfs(root,-999999999,99999999999)
        return isValid