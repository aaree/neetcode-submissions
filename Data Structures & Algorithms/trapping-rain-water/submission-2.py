class Solution:
    def trap(self, height: List[int]) -> int:
        maxheight=max(height)
        maxHeightLocation=0
        for i,val in enumerate(height):
            if val==maxheight:
                maxHeightLocation=i
                break
        l=0
        r=len(height)-1
        totalRain=0
        lheight=0
        rheight=0
        while l<maxHeightLocation:
            if (lheight-height[l])>0:                
                totalRain+=(lheight-height[l])
                print(totalRain)
            lheight=max(lheight,height[l])
            l+=1
        while r>maxHeightLocation:
            if (rheight-height[r])>0:
                totalRain+=(rheight-height[r])
            rheight=max(rheight,height[r])
            r-=1
        return totalRain