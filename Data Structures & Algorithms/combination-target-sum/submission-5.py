class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]

        def dfs(arr,t,position):
            if t==0:
                ans.append(arr.copy())
                return
            if t<0:
                return
            for i in range(position,len(nums)):
                arr.append(nums[i])
                dfs(arr,t-nums[i],i)
                arr.pop()
        dfs([],target,0)
        return ans