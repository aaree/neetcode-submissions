class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)
        ans=[]
        heap=[]
        heapq.heapify(heap)
        countDown={}
        tempArr=[]
        for key, val in c.items():
            heapq.heappush(heap,(-val,key))
            countDown[key]=None
        while len(heap)>0:
            temp=n
            num,let=heapq.heappop(heap)
            if countDown[let] is None or (len(ans)-countDown[let]>n-1):
                ans.append(let)
                if (num+1)<0:
                    heapq.heappush(heap,(num+1,let))
                countDown[let]=len(ans)
            else:
                notFound=True
                while len(heap)>0:
                    tempArr.append((num,let))
                    num,let=heapq.heappop(heap)
                    if countDown[let] is None or (len(ans)-countDown[let]>n-1):
                        notFound=False
                        ans.append(let)
                        countDown[let]=len(ans)
                        if (num+1)<0:
                            heapq.heappush(heap,(num+1,let))
                        break
                if notFound:
                    ans.append(None)
                    heapq.heappush(heap,(num,let))            
                while len(tempArr)>0:
                    num,let=tempArr.pop()
                    heapq.heappush(heap,(num,let))
        return len(ans)



        