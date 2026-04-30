class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans=[]
        seen=set()
        loop=set()
        adj={}
        for i in range(numCourses):
            adj[i]=[]
        for start,end in prerequisites:
            adj[start].append(end)
        def dfs(node):
            if node in loop:
                return False
            if node in seen:
                return True
            loop.add(node)
            if node in adj:
                for c in adj[node]:
                    if not dfs(c):
                        return False
            seen.add(node)
            loop.remove(node)
            ans.append(node)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return ans
            
