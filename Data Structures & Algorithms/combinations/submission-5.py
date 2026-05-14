class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        arr=range(1,n+1)
        def backtrack(nums,pointer):
            if len(nums)==k:
                ans.append(nums.copy())
                return
            if pointer>=len(arr):
                return
            nums.append(arr[pointer])
            backtrack(nums,pointer+1)
            nums.pop()
            backtrack(nums,pointer+1)
        backtrack([],0)
        return ans