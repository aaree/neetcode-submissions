class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        loop=set()
        seen=set()
        adj={}
        answer=[]
        for c in range(numCourses):
            adj[c]=[]
        for a,b in prerequisites:
            adj[a].append(b)
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
            answer.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return answer

