class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while r>=l:
            print(l,r)            
            m=(r+l)//2
            mid=nums[m]
            print(mid)
            if mid==target:
                return m
            if mid>nums[-1]:
                if nums[0]<=target and mid>=target:
                    r=m-1
                else:
                    l=m+1
                    print(l,r)
            else:
                if nums[-1]>=target and mid<=target:
                    l=m+1
                else:
                    r=m-1
        return -1