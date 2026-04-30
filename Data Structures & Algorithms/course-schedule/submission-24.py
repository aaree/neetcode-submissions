class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen=set()
        ans=[]
        loop=set()
        preReq={}
        allCourses=set(range(numCourses))
        for a,b in prerequisites:
            if a not in preReq:
                preReq[a]=[]
            preReq[a].append(b)
        def dfs(course):
            nonlocal loop
            if course in loop:
                return False
            if course in seen:
                return True
            
            loop.add(course)
            if course in preReq:
                for c in preReq[course]:
                    if not dfs(c):
                        return False
            seen.add(course)
            loop.remove(course)
            ans.append(course)
            return True


        for course in allCourses:
            test=dfs(course)
            if test==False:
                return False
        return True