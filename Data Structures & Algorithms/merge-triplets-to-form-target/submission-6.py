class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        mina=math.inf
        minb=math.inf
        minc=math.inf
        maxa=0
        maxb=0
        maxc=0
        for i in triplets:
            if i==target:
                return True
            if i[0]<=target[0] and i[1]<=target[1] and i[2]<=target[2]:
                maxa=max(i[0],maxa)
                maxb=max(i[1],maxb)
                maxc=max(i[2],maxc)
                mina=min(i[0],mina)
                minb=min(i[1],minb)
                minc=min(i[2],minc)
        if ( maxa<target[0] or maxb<target[1] or maxc<target[2]):
            return False
        return True