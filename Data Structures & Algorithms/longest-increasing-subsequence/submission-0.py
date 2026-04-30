class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[]
        seen=set()
        def backtrack(arr,pointer):
            if pointer==len(nums) and tuple(arr) not in seen:
                seen.add(tuple(arr.copy()))
                ans.append(arr.copy())
                return
            while pointer<len(nums):
                if len(arr)==0 or nums[pointer]>arr[-1]:
                    arr.append(nums[pointer])
                    backtrack(arr,pointer+1)
                    arr.pop()
                else:
                    backtrack(arr,pointer+1)
                pointer+=1
        
        
        backtrack([],0)
        ans.sort(key=lambda x:-len(x))
        return len(ans[0])