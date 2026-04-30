class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if nums[0]==0:
            return False
        nums.reverse()
        pointer=0
        for i, val in enumerate(nums):
            if i-val<=pointer:
                pointer=i
        if pointer==len(nums)-1:
            return True
        return False
            