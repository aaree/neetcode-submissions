class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left=0
        for i, num in enumerate(nums):
            if num!=val:
                nums[i],nums[left]=nums[left],nums[i]
                left+=1
        return left