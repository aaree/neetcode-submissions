class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        while r>=l:
            m=(r+l)//2
            mid=matrix[m]
            if mid[0]>target:
                r=m-1
            elif mid[-1]<target:
                l=m+1
            elif mid[0]<=target<=mid[-1]:
                l2=0
                r2=len(matrix[0])-1
                while r2>=l2:
                    m2=(l2+r2)//2
                    mid2=matrix[m][m2]
                    if mid2>target:
                        r2=m2-1
                    elif mid2<target:
                        l2=m2+1
                    elif mid2==target:
                        return True
                break      
        return False