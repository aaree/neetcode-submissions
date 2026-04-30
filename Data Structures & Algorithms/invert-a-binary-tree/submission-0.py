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
        head=root
        c=TreeNode(root.val)
        arr=deque()
        carr=deque()
        arr.append(head)
        carr.append(c)
        while len(arr)>0:
            for i in range(len(arr)):
                node=arr.popleft()
                copy=carr.popleft()
                if node.left:
                    copy.right=TreeNode(node.left.val)
                    arr.append(node.left)
                    carr.append(copy.right)
                if node.right:
                    copy.left=TreeNode(node.right.val)
                    arr.append(node.right)
                    carr.append(copy.left)
            for i in arr:
                print(i.val)
            print('///')
        return c
