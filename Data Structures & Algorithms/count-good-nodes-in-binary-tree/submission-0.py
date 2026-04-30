# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt=0
        def dfs(node,val):
            nonlocal cnt
            new_val=val
            if node is None:
                return
            if node.val>=val:
                cnt+=1
                new_val=node.val
            dfs(node.left,new_val)
            dfs(node.right,new_val)
        dfs(root,root.val)
        return cnt
