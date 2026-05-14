class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        seen=set()
        adj={}
        for i in range(numCourses):
            adj[i]=[]
        for a,b in prerequisites:
            adj[a].append(b)

        def dfs(course,target):
            if course==target:
                return True
            if (course,target) in seen:
                return False
            if course in adj:
                for c in adj[course]:
                    if dfs(c,target):
                        return True
            seen.add((course,target))
        final=[]
        for a,b in queries:
            res=dfs(a,b)
            if res is None:
                res=False
            final.append(res)
            seen=set()
        return final
        