class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxDist=0
        minval=arrays[0][0]
        maxval=arrays[0][-1]
        for i in range(1,len(arrays)):
            d1=abs(maxval-arrays[i][0])
            d2=abs(arrays[i][-1]-minval)
            d=max(d1,d2)
            maxDist=max(maxDist,d)
            minval=min(arrays[i][0],minval)
            maxval=max(arrays[i][-1],maxval)
        return maxDist