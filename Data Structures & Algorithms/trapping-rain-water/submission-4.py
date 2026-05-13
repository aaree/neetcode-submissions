class Solution:
    def trap(self, height: List[int]) -> int:
        maxHeight=(0,0)
        for i, val in enumerate(height):
            if val>maxHeight[1]:
                maxHeight=(i,val)
        leftVol=0
        maxLeft=0
        for i in range(maxHeight[0]):
            maxLeft=max(maxLeft,height[i])
            leftVol+=maxLeft-height[i]
        rightVol=0
        maxRight=0
        for i in range(len(height)-1,maxHeight[0],-1):
            maxRight=max(maxRight,height[i])
            rightVol+=maxRight-height[i]
        return leftVol+rightVol