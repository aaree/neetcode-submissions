class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        while len(nums)>0 and nums[-1]==val:
            nums.pop()
        i=0
        while i<len(nums):
            num=nums[i]
            if num==val:
                nums[i],nums[-1]=nums[-1],nums[i]
                nums.pop()
            else:
                i+=1
        if not nums:
            return 0
        return len(nums)