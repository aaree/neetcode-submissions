class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        allNum=set(range(1,n+1))
        seen=set()
        def backtrack(pointer,combo):
            if tuple(combo) not in seen and len(combo)==k:
                seen.add(tuple(combo))
                ans.append(sorted(combo.copy()))
                return
            for i in allNum:
                if len(combo)==0 or i>combo[-1]:
                    combo.append(i)
                    allNum.remove(i)
                    backtrack(allNum,combo)
                    allNum.add(i)
                    combo.pop()
        backtrack(0,[])
        ans.sort()
        return ans

            
