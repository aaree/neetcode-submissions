class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seen=set()
        ans=[]
        def backtrack(combo,num):
            
            #print(combo)
            if len(combo)==len(nums) and tuple(combo) not in seen:
                seen.add(tuple(combo.copy()))
                ans.append(combo.copy())
            for i, val in enumerate(num):
                combo.append(val)
                #print(num,val)
                if i!=len(num)-1:
                    num[i],num[-1]=num[-1],num[i]
                num.pop()
                #print(num)
                backtrack(combo.copy(),num.copy())
                combo.pop()
                num.append(val)
                num[i],num[-1]=num[-1],num[i]
        backtrack([],nums.copy())
        return ans


