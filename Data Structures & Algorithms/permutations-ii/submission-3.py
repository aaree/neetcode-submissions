class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seen=set()
        ans=[]
        used=[False]*len(nums)
        def backtrack(combo,num,used):
            
            #print(combo)
            if len(combo)==len(nums):
                ans.append(combo.copy())
            for i, val in enumerate(num):
                if used[i]:
                    continue
                if i==0 or num[i]!=num[i-1] or (num[i]==num[i-1] and used[i-1]==False):
                    combo.append(val)
                    used[i]=True
                    backtrack(combo.copy(),num.copy(),used.copy())
                    used[i]=False
                    combo.pop()
        backtrack([],sorted(nums.copy()),used)
        return ans


