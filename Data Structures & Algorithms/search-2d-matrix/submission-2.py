class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        while r>=l:
            m=(r+l)//2
            mid=matrix[m]
            if mid[-1]<target:
                l=m+1
            elif mid[0]>target:
                r=m-1
            elif mid[0]<=target and mid[-1]>=target:
                break
        if mid[0]>target or mid[-1]<target:
            return False
        l=0
        r=len(mid)-1
        while r>=l:
            m=(l+r)//2
            middle=mid[m]
            if middle>target:
                r=m-1
            elif middle<target:
                l=m+1
            elif middle==target:
                return True
        return False