# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return
        root=TreeNode(preorder[0])
        index=inorder.index(preorder[0])
        left=inorder[:index]
        right=inorder[index+1:]
        preorder_left=preorder[1:len(left)+1]
        preorder_right=preorder[1+len(left):]
        root.left=self.buildTree(preorder_left,left)
        root.right=self.buildTree(preorder_right,right)
        return root