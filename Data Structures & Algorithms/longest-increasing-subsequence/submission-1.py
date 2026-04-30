class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[]
        seen=set()
        memo={}
        def backtrack(arr,pointer):
            if (tuple(arr.copy()),pointer) in memo:
                return memo[(tuple(arr.copy()),pointer)]
            if pointer==len(nums) and tuple(arr) not in seen:
                seen.add(tuple(arr.copy()))
                ans.append(arr.copy())
                memo[(tuple(arr.copy()),pointer)]=len(arr.copy())
                return memo[(tuple(arr.copy()),pointer)]
            while pointer<len(nums):
                if len(arr)==0 or nums[pointer]>arr[-1]:
                    arr.append(nums[pointer])
                    backtrack(arr,pointer+1)
                    arr.pop()
                else:
                    backtrack(arr,pointer+1)
                pointer+=1
        
        
        backtrack([],0)
        maxVal=0
        for key, val in memo.items():
            maxVal=max(val,maxVal)
        return maxVal        