class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        values=set(nums)
        temp=[0]*(max(nums)+1)
        for i in nums:
            if i in values:
                temp[i]+=1
        pointer=0
        pointer2=0
        while pointer2<len(nums):
            while temp[pointer]>0:
                nums[pointer2]=pointer
                temp[pointer]-=1
                pointer2+=1
            pointer+=1
        

