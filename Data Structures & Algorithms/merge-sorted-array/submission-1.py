class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.pop()
        for i in range(n):
            nums1.append(nums2[i])
        for i in range(1,len(nums1)):
            j=i-1
            while j>=0 and nums1[j+1]<nums1[j]:
                nums1[j+1],nums1[j]=nums1[j],nums1[j+1]
                j-=1
        
        
            