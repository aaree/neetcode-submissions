class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while r>=l:
            m=(r+l)//2
            mid=nums[m]
            if mid>target:
                r=m-1
            elif mid<target:
                l=m+1
            elif mid==target:
                return m
        return -1