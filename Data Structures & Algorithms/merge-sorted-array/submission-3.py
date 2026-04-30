class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1)>0 and nums1[-1]==0:
            nums1.pop()
        nums1.extend(nums2)
        def mergeSort(arr,s,e):
            def merge(arr,s,m,e):
                L=arr[s:m+1]
                R=arr[m+1:e+1]
                i=j=0
                k=s
                while i<len(L) and j<len(R):
                    if L[i]<=R[j]:
                        arr[k]=L[i]
                        i+=1
                    else:
                        arr[k]=R[j]
                        j+=1
                    k+=1
                while i<len(L):
                    arr[k]=L[i]
                    i+=1
                    k+=1
                while j<len(R):
                    arr[k]=R[j]
                    j+=1
                    k+=1

            if e-s+1<=1:
                return arr
            m=(s+e)//2
            mergeSort(arr,s,m)
            mergeSort(arr,m+1,e)
            merge(arr,s,m,e)
        mergeSort(nums1,0,len(nums1)-1)