# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy=root
        queue=deque()
        queue.append(dummy)
        while len(queue)>0:
            for i in range(len(queue)):
                curr=queue.popleft()
                if curr:
                    curr.left,curr.right=curr.right,curr.left
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
        return root