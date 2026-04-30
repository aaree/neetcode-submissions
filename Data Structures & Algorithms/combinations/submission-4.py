class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        allNum=set(range(1,n+1))
        seen=set()
        def backtrack(combo):
            if len(combo)==k:
                ans.append(combo.copy())
                return
            for i in allNum:
                if len(combo)==0 or i>combo[-1]:
                    combo.append(i)
                    allNum.remove(i)
                    backtrack(combo)
                    allNum.add(i)
                    combo.pop()
        backtrack([])
        return ans

            
