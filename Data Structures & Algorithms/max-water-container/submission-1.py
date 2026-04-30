class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxArea=0
        while r>l:
            h=min(heights[r],heights[l])
            area=h*(r-l)
            maxArea=max(area,maxArea)
            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1
        return maxArea
