class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxArea=0
        while r>l:
            width=r-l
            height=min(heights[r],heights[l])
            maxArea=max(maxArea,width*height)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxArea