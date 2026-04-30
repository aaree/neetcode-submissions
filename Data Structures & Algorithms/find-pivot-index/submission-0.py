class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans=[0]
        for i in nums:
            ans.append(ans[-1]+i)
        print(ans)
        for i, val in enumerate(ans):
            if i<len(nums):
                if val==(ans[-1]-nums[i])/2:
                    return i
        return -1