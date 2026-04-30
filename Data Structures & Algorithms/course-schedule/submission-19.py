class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites)==0:
            return True
        canstart=set(range(numCourses))
        preReq={}
        block={}
        for a,b in prerequisites:
            if b in canstart:
                canstart.remove(b)
            if a not in preReq:
                preReq[a]=[]
            if b not in block:
                block[b]=set()
            preReq[a].append(b)
            block[b].add(a)
        if len(canstart)==0:
            return False
        taken=list(canstart)
        seen=set()
        queue=deque()
        for i in canstart:
            queue.append(i)
            seen.add(i)
        while len(queue)>0:
            curr=queue.popleft()
            if curr in preReq:
                next=preReq[curr]
            else:
                next=[]
            for val in next:
                if val not in seen:
                    if val in block:
                        block[val].remove(curr)
                    if len(block[val])==0:
                        seen.add(val)
                        taken.append(val)
                        queue.append(val)
        return len(taken)==numCourses

