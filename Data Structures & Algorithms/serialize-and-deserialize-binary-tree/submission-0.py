# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        queue=deque()
        queue.append(root)
        ans=[]
        while len(queue)>0:
            for i in range(len(queue)):
                curr=queue.popleft()
                if curr:
                    ans.append(str(curr.val))
                else:
                    ans.append('empty')
                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
        print(','.join(ans))
        return ','.join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=='':
            return None
        ans=data.split(',')
        rootval=ans[0]
        if rootval!='empty':
            rootval=int(rootval)
        root=TreeNode(rootval)
        pointer=1
        dummy=root
        queue=deque()
        queue.append(dummy)
        while len(queue)>0:
            for i in range(len(queue)):
                curr=queue.popleft()
                if ans[pointer] != 'empty' and pointer<len(ans):
                    curr.left=TreeNode(int(ans[pointer]))
                    queue.append(curr.left)
                pointer+=1
                if ans[pointer]!='empty' and pointer<len(ans):
                    curr.right=TreeNode(int(ans[pointer]))
                    queue.append(curr.right)
                pointer+=1
        return root