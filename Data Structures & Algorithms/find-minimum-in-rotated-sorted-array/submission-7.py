class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while r>l:
            m=(r+l)//2
            mid=nums[m]
            if mid>=nums[-1]:
                l=m+1
            else:
                r=m
        return nums[l]