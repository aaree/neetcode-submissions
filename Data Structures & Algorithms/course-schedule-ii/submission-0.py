class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans=[]
        seen=set()
        preReq={}
        allCourse=range(numCourses)
        for a, b in prerequisites:
            if a not in preReq:
                preReq[a]=[]
            preReq[a].append(b)
        loop=set()

        def dfs(course):
            if course in loop:
                return False
            if course in seen:
                return True
            loop.add(course)
            if course in preReq:
                for c in preReq[course]:
                    if not dfs(c):
                        return False
            ans.append(course)
            loop.remove(course)
            seen.add(course)
            print(course)
            return True
        
        for course in allCourse:
            temp=dfs(course)
            if not temp:
                return []
        return ans