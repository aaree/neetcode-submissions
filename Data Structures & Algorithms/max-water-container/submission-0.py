class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max_area=0
        while right>left:
            area=min(heights[left],heights[right])*(right-left)
            max_area=max(area,max_area)
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return max_area