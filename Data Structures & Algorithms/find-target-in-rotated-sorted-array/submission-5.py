class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        l=0
        r=len(nums)-1

        while r>l:
            m=(r+l)//2
            mid=nums[m]
            if mid==target:
                return m
            if mid>nums[-1]:
                if nums[0]<=target<=mid:
                    r=m-1
                else:
                    l=m+1
            elif mid<nums[-1]:
                if mid<=target<=nums[-1]:
                    l=m+1
                else:
                    r=m-1
        
        if nums[l]==target:
            return l
        else:
            return -1
