class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[]
        seen=set()
        memo={}
        def backtrack(previous,pointer,cnt):
            if (previous,pointer,cnt) in memo:
                return memo[(previous,pointer,cnt)]
            if pointer==len(nums):
                memo[(previous,pointer,cnt)]=cnt
                return memo[(previous,pointer,cnt)]
            while pointer<len(nums):
                if previous=='' or nums[pointer]>previous:
                    backtrack(nums[pointer],pointer+1,cnt+1)
                else:
                    backtrack(previous,pointer+1,cnt)
                pointer+=1
        
        
        backtrack('',0,0)
        maxVal=0
        for key, val in memo.items():
            maxVal=max(val,maxVal)
        return maxVal        