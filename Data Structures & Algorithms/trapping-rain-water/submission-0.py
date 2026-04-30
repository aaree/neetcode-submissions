class Solution:
    def trap(self, height: List[int]) -> int:
        maxlevel=0
        location=0
        for num,val in enumerate(height):
            if val>maxlevel:
                maxlevel=max(maxlevel,val)
                location=num
        l=0
        r=len(height)-1
        leftwater=0
        left_max=0
        while l<location:
            leftwater+=max(left_max-height[l],0)
            left_max=max(left_max,height[l])
            l+=1
        rightwater=0
        right_max=0
        while r>location:
            rightwater+=max(right_max-height[r],0)
            right_max=max(right_max,height[r])
            r-=1
        return leftwater+rightwater