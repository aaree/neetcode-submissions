class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        loop=set()
        seen=set()
        adj={}
        pmap={}
        ans=[]
        for i in range(numCourses):
            adj[i]=[]
        for a,b in prerequisites:
            adj[b].append(a)
        def dfs(course):
            if course not in pmap:
                pmap[course]=set()
                if course in adj:
                    for c in adj[course]:
                        pmap[course].update(dfs(c))
                pmap[course].add(course)
            return pmap[course]


        for num in range(numCourses):
            dfs(num)
        for u, v in queries:
            ans.append(u in pmap[v])
        return ans
