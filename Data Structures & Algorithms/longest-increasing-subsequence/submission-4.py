class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[]
        seen=set()
        memo={}
        def backtrack(previous,pointer):
            if (previous,pointer) in memo:
                return memo[(previous,pointer)]
            if pointer==len(nums):
                memo[(previous,pointer)]=0
                return memo[(previous,pointer)]
            if previous=='' or nums[pointer]>previous:
                memo[(previous,pointer)]=max(backtrack(nums[pointer],pointer+1)+1,backtrack(previous,pointer+1))
            else:
                memo[(previous,pointer)]=backtrack(previous,pointer+1)
            return memo[(previous,pointer)]
        
        backtrack('',0)
        maxVal=0
        for key, val in memo.items():
            maxVal=max(val,maxVal)
        return maxVal        