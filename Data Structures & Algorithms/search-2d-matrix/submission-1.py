class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L=0
        R=len(matrix)
        val=0
        while R>=L:
            mid=(L+R)//2
            if mid+1>len(matrix):
                return False
            mid_min=matrix[mid][0]
            mid_max=matrix[mid][-1]
            if mid_min>target:
                R=mid-1
            elif mid_max<target:
                L=mid+1
            else:
                break
        if target<mid_min or target>mid_max:
            return False
        search=matrix[mid]
        L=0
        R=len(search)
        while R>=L:
            mid=(L+R)//2
            middle=search[mid]
            if middle>target:
                R=mid-1
            elif middle<target:
                L=mid+1
            else:
                return True
        return False
