class Solution:
    def trap(self, height: List[int]) -> int:
        maxVal=0
        maxLoc=0
        for i, val in enumerate(height):
            if val>maxVal:
                maxVal=val
                maxLoc=i
        left=0
        right=len(height)-1
        leftHeight=0
        total=0
        while left<maxLoc:
            total+=max(leftHeight-height[left],0)
            leftHeight=max(leftHeight,height[left])
            left+=1
        rightHeight=0
        while right>maxLoc:
            total+=max(rightHeight-height[right],0)
            rightHeight=max(rightHeight,height[right])
            right-=1
        return total
        