class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        for i in points:
            print(i)
            val=math.sqrt(i[0]**2+i[1]**2)
            print(val)
            ans.append((val,i))
        heapq.heapify(ans)
        a=[]
        for i in range(k):
            value=heapq.heappop(ans)
            a.append(value[1])
        return a