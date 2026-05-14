class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={}
        for i in range(numCourses):
            adj[i]=[]
        for a,b in prerequisites:
            adj[a].append(b)

        seen=set()
        loop=set()
        ans=[]
        def dfs(course):
            if course in loop:
                return False
            if course in seen:
                return True
            
            loop.add(course)
            if course in adj:
                for c in adj[course]:
                    if not dfs(c):
                        return False

            loop.remove(course)
            seen.add(course)
            ans.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans