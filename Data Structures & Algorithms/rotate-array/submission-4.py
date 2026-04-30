class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp=[None]*len(nums)
        for i,val in enumerate(nums):
            tmp[(i+k)%len(nums)]=val
        nums[:]=tmp