# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        bfs=deque()
        ans=[]
        bfs.append(root)
        ans.append(root.val)
        while len(bfs)>0:
            new=[]
            for i in range(len(bfs)):
                curr=bfs.popleft()
                if curr.left:
                    new.append(curr.left.val)
                    bfs.append(curr.left)
                if curr.right:
                    new.append(curr.right.val)
                    bfs.append(curr.right)
            if len(new)>0:
                ans.append(new[-1])
        return ans