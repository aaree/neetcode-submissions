class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp=[]
        for i in arr:
            diff=abs(i-x)
            temp.append((diff,i))
        heapq.heapify(temp)
        final=[]
        for i in range(k):
            num,val=heapq.heappop(temp)
            final.append(val)
        return sorted(final)

