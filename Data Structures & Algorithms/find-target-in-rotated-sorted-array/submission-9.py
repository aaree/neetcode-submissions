class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        l=0
        r=len(nums)-1

        while r>=l:            
            m=(r+l)//2
            mid=nums[m]
            if mid==target:
                return m
            if nums[l]<=mid:
                if nums[l]<=target<mid:
                    r=m-1
                else:
                    l=m+1
            else:
                if mid<target<=nums[r]:
                    l=m+1
                else:
                    r=m-1

        return -1
