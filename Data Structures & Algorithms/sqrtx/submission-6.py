class Solution:
    def mySqrt(self, x: int) -> int:
        arr=range(1,x+1)
        l=0
        r=len(arr)-1
        while r>=l:
            m=(r+l)//2
            mid=arr[m]
            if mid*mid==x:
                return mid
            if mid*mid>x:
                r=m-1
            else:
                l=m+1
        return l