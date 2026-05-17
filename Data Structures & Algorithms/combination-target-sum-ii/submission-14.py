class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        seen=[]

        def dfs(arr,i,curr):
            if curr==target:
                seen.append(arr.copy())
                return
            if curr>target or i==len(candidates):
                return
            arr.append(candidates[i])
            dfs(arr,i+1,curr+candidates[i])
            arr.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(arr,i+1,curr)
        dfs([],0,0)
        return seen