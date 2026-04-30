class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums.reverse()
        left=right=0
        while right<len(nums)-1:
            right+=1
            if right-nums[right]<=left:
                left=right
        print(left)
        if left==len(nums)-1:
            return True
        else:
            return False        