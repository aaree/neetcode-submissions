class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def backtrack(num,s):
            nonlocal target
            nonlocal ans
            if sum(s)==target and sorted(s) not in ans:
                s=sorted(s)
                ans.append(s.copy())
            if sum(s)>target:
                return False
            for i in num:
                s.append(i)
                backtrack(num,s.copy())
                s.pop()        
        backtrack(nums,[])
        return ans