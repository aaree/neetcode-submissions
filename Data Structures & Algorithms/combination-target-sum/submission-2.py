class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=set()
        def backtrack(arr):
            if sum(arr)>target:
                return
            elif sum(arr)==target:
                ans.add(tuple(sorted(arr)))            
            for i in nums:
                arr.append(i)
                backtrack(arr.copy())
                arr.pop()
        backtrack([])
        final=[]
        for i in ans:
            final.append(list(i))
        return final
        