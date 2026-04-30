# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca=None
        def dfs(node):
            nonlocal lca
            print(node.val)
            if (p.val<=node.val and q.val>=node.val) or (q.val<=node.val and p.val>=node.val):
                lca=node
            if p.val>node.val and q.val>node.val:
                dfs(node.right)
            if p.val<node.val and q.val<node.val:
                dfs(node.left)
        dfs(root)
        return lca