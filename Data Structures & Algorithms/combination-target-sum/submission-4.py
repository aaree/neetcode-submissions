class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def dfs(arr,i):
            if i>=len(nums):
                return
            if sum(arr)==target:
                ans.append(arr.copy())
                return
            elif sum(arr)>target:
                return
            arr.append(nums[i])
            dfs(arr,i)
            arr.pop()
            dfs(arr,i+1)
        
        dfs([],0)
        return ans