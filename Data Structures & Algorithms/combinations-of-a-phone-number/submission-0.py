class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        mapping={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        ans=[]
        seen=set()
        def backtrack(s,pointer):
            if len(s)==len(digits) and ''.join(s) not in seen:
                seen.add(''.join(s))
                ans.append(''.join(s))
                return
            arr=mapping[digits[pointer]]
            for i in arr:
                s.append(i)
                backtrack(s,pointer+1)
                s.pop()
        backtrack([],0)
        return ans
            