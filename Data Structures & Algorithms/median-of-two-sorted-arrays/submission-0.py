class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total=len(nums1)+len(nums2)
        half=total//2
        a,b=nums1,nums2
        if len(a)>len(b):
            b,a=a,b
        l=0
        r=len(a)-1
        print(a)
        print(b)
        while True:
            print(r,l)
            m=(r+l)//2
            j=half-m-2
            Aleft=a[m] if m>=0 else float("-inf")
            Aright=a[m+1] if m+1<len(a) else float("inf")
            Bleft=b[j] if j>=0 else float("-inf")
            Bright=b[j+1] if (j+1)<len(b) else float("inf")

            if Aleft<=Bright and Bleft<=Aright:
                if total%2==1:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r=m-1
            else:
                l=m+1