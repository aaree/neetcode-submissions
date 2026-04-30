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
        queue=deque()
        queue.append(root)
        clone_top=TreeNode(root.val)
        c=clone_top
        queue2=deque()
        queue2.append(c)
        while len(queue)>0:
            for i in range(len(queue)):
                curr=queue.popleft()
                clone=queue2.popleft()
                if curr.left:
                    queue.append(curr.left)
                    new=TreeNode(curr.left.val)
                    clone.right=new
                    queue2.append(new)
                if curr.right:
                    queue.append(curr.right)
                    new=TreeNode(curr.right.val)
                    clone.left=new
                    queue2.append(new)
        return clone_top

