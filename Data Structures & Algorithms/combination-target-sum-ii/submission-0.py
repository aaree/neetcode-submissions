class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=set()
        def backtrack(arr,pointer):
            if sum(arr)>target:
                return
            elif sum(arr)==target:
                ans.add(tuple(sorted(arr)))
                return
            while pointer<len(candidates):
                arr.append(candidates[pointer])
                backtrack(arr.copy(),pointer+1)
                arr.pop()
                pointer+=1
        backtrack([],0)
        final=[]
        for i in ans:
            final.append(list(i))
        return final