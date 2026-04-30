class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def backtrack(arr,pointer):
            if sum(arr)>target:
                return
            elif sum(arr)==target:
                ans.append(arr)            
            while pointer<len(nums):
                arr.append(nums[pointer])
                backtrack(arr.copy(),pointer)
                arr.pop()
                pointer+=1
        backtrack([],0)
        return ans
        