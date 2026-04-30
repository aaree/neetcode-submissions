class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=[None]*len(nums)
        for i, val in enumerate(nums):
            temp[(i+k)%len(nums)]=val
        nums[:]=temp