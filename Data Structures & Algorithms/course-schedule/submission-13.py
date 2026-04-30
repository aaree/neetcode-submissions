class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites)==0:
            return True
        pre=set()
        total=set()
        total2=set()
        routes=[]
        seen=set()
        seen2=set()
        for i in prerequisites:
            pre.add(i[0])
            total.add(i[0])
            total.add(i[1])
            total2.add(i[0])
            total2.add(i[1])
            routes.append(i)
        total.difference_update(pre)
        if len(total)==0:
            return False
        def dfs(course,s):
            prereq=False
            nonlocal routes
            nonlocal seen
            nonlocal pre
            if len(seen)==len(total2):
                return
            for i in routes:
                prereq=False
                if i[1]==course:
                    if i[0] in pre:
                        for j in routes:
                            if j[0]==i[0] and j[1] not in s:
                                
                                prereq=True
                                
                    if prereq==True:
                        continue
                    elif i[0] in s:
                        for i in s:
                            seen.add(i)
                        return
                    else:
                        s.add(i[0])
                        dfs(i[0],s)

            for i in s:
                seen.add(i)
            return
        for i in list(total):
            seen.add(i)
            dfs(i,seen)
        print(seen)
        return len(seen)==len(total2)
