class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxDist=0
        for i in range(1,len(arrays)):
            j=i-1
            v1=arrays[j][0]
            v2=arrays[i][-1]
            d1=abs(v2-v1)
            v3=arrays[j][-1]
            v4=arrays[i][0]
            d2=abs(v3-v4)
            d=max(d1,d2)
            maxDist=max(maxDist,d)
        return maxDist