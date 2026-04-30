class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={}
        for i in range(numCourses):
            adj[i]=[]
        for a,b in prerequisites:
            adj[a].append(b)
        seen=set()
        loop=set()

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
            loop.remove(node)
            seen.add(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True