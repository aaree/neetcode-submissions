class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack=[]
        for pos,height in enumerate(heights):
            if len(stack)==0:
                stack.append([pos,height])
                maxArea=height
            elif height<stack[-1][1]:
                while len(stack)>0 and height<stack[-1][1]:
                    oldpos,oldheight=stack.pop()
                    maxArea=max(maxArea,(pos-oldpos)*oldheight)
                stack.append([oldpos,height])
            else:
                stack.append([pos,height])
        length=len(heights)
        for pos,height in stack:
            maxArea=max(maxArea,(length-pos)*height)
        return maxArea