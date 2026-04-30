class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while r>=l:
            m=(r+l)//2
            mid=nums[m]
            if mid==target:
                return m
            if mid<nums[-1]:
                rotated=False
            else:
                rotated=True
            if rotated:
                if nums[0]<=target<mid:
                    r=m-1
                else:
                    l=m+1
            if not rotated:
                if mid<target<=nums[-1]:
                    l=m+1
                else:
                    r=m-1
        return -1
