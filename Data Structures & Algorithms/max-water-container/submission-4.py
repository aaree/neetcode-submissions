class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxVolume=0
        while right>left:
            volume=(right-left)*min(heights[left],heights[right])
            maxVolume=max(volume,maxVolume)
            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
        return maxVolume